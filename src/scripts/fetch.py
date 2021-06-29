import sqlite3
import os


def artist_albums(artist_id: str):
    BASE_DIR = os.getcwd()
    DB_DIR = "src/database/rezo.db"
    DB_PATH = os.path.join(BASE_DIR, DB_DIR)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    SQL = """
          SELECT * FROM albums
          WHERE artist_id = ?
          ORDER by album_popularity DESC
          LIMIT 50
          """
    cur.execute(SQL, (artist_id, ))

    res = cur.fetchall()
    dict_list = []
    for album in res:
        album_dict = {
            "artist_name": album[0],
            "album_name": album[1],
            "album_id": album[2],
            "artist_id": album[3],
            "album_img": album[4],
            "album_popularity": album[5]
        }
        dict_list.append(album_dict)
    
    cur.close()
    conn.close()
    return dict_list



def albums_tracks(album_id: str):
    BASE_DIR = os.getcwd()
    DB_DIR = "src/database/rezo.db"
    DB_PATH = os.path.join(BASE_DIR, DB_DIR)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    SQL = """
          SELECT * from tracks_fts4
          WHERE album_id=?
          LIMIT 50
          """
    cur.execute(SQL, (album_id, ))

    tracks = cur.fetchall()
    tracks_list = []
    for track in tracks:
        track_dict ={
            "ref_id": track[0],
            "track_name": track[3],
            "track_id": track[2],
            "track_url": track[5]
        }
        tracks_list.append(track_dict)

    cur.close()
    conn.close()
    return tracks_list


