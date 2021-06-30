import sqlite3
import sqlite_spellfix
import json
import redis
import datetime
import os


def search_tracks(param):
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    cached_data = redis_client.get(param)
    if cached_data is not None:
        json_data = json.loads(cached_data)
        return json_data

    else:
        BASE_DIR = os.getcwd()
        DB_DIR = "src/database/rezo.db"
        DB_PATH = os.path.join(BASE_DIR, DB_DIR)
        conn = sqlite3.connect(DB_PATH)
        conn.enable_load_extension(True)
        conn.load_extension(sqlite_spellfix.extension_path())
        cur = conn.cursor()
        correctedquery = []
        for term in param.split():
            spellfix_query = "SELECT word FROM tracks_spell WHERE word MATCH ? and top=1"
            cur.execute(spellfix_query, (term,))
            r = cur.fetchone()
            correctedquery.append(r[0] if r is not None else term)  # correct the word if any match in the spellfix table; if no match, keep the word spelled as it is (then the search will give no result!)
        
        correctedquery = ' '.join(correctedquery)
        correctedquery += '*'
        cur.execute(
            """
            SELECT ref_id, track_name, a.album_name, art.artist_name, t.track_url, a.album_img, t.track_id
            FROM tracks_fts4 t
            INNER JOIN albums a
            ON t.album_id = a.album_id
            INNER JOIN artists art
            ON a.artist_id = art.artist_id
            WHERE tracks_fts4
            MATCH ?
            ORDER BY art.artist_popularity DESC
            LIMIT 50
            """, (correctedquery, )
        )

        dict_list = []
        for item in cur.fetchmany(50):
            item_dict = {
                "ref_id": item[0],
                "track_name": item[1],
                "album_name": item[2],
                "artist_name": item[3],
                "track_url": item[4],
                "album_image": item[5],
                "track_id": item[6]
            }
            dict_list.append(item_dict)

        unq_list = list({track['track_id']:track for track in dict_list}.values())
        cur.close()
        conn.close()
        redis_client.setex(param, datetime.timedelta(hours=12), json.dumps(unq_list))
        return unq_list
        


def search_artists(param):
    redis_client = redis.Redis(host='localhost', port=6379, db=1)
    cached_data = redis_client.get(param)

    if cached_data is not None:    
        json_data = json.loads(cached_data)
        return json_data

    else:
        BASE_DIR = os.getcwd()
        DB_DIR = "src/database/rezo.db"
        DB_PATH = os.path.join(BASE_DIR, DB_DIR)
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute(
                """
                SELECT * FROM artists
                WHERE artist_name
                LIKE ('%' || ? || '%')
                ORDER BY artist_popularity DESC
                LIMIT 50
                """, (param, )
                    )
        
        dict_list = []
        query_result = cur.fetchall()

        for item in query_result:
            item_dict = {
                "artist_id": item[0],
                "artist_name": item[1],
                "artist_image": item[4],
            }
            dict_list.append(item_dict)
        conn.close()
        redis_client.setex(param, datetime.timedelta(days=7), json.dumps(dict_list))
        return dict_list



def search_albums(param):
    redis_client = redis.Redis(host='localhost', port=6379, db=2)
    cached_data = redis_client.get(param)

    if cached_data is not None:    
        json_data = json.loads(cached_data)
        return json_data

    else:
        BASE_DIR = os.getcwd()
        DB_DIR = "src/database/rezo.db"
        DB_PATH = os.path.join(BASE_DIR, DB_DIR)
        conn = sqlite3.connect(DB_PATH)
        conn.enable_load_extension(True)
        conn.load_extension(sqlite_spellfix.extension_path())
        cur = conn.cursor()
        
        correctedquery = []
        for term in param.split():
            spellfix_query = "SELECT word FROM albums_spell WHERE word MATCH ? and top=1"
            cur.execute(spellfix_query, (term,))
            r = cur.fetchone()
            correctedquery.append(r[0] if r is not None else term)  # correct the word if any match in the spellfix table; if no match, keep the word spelled as it is (then the search will give no result!)
        
        correctedquery = ' '.join(correctedquery)
        correctedquery += '*'

        cur.execute(
                """
                SELECT * FROM albums_fts4
                WHERE albums_fts4
                MATCH ?
                ORDER BY album_popularity DESC
                LIMIT 50
                """, (correctedquery, )
                    )
        
        dict_list = []
        query_result = cur.fetchall()
        for album in query_result:
            album_dict = {
                'artist_id': album[0],
                'album_id': album[1],
                'album_img': album[2],
                'artist_name': album[4],
                'album_name': album[5],
            }
            dict_list.append(album_dict)
            
        cur.close()
        conn.close()
        redis_client.setex(param, datetime.timedelta(days=1), json.dumps(dict_list))
        return dict_list

