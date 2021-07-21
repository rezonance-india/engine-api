import sqlite3
import numpy as np
import random
import os

def track_url_encoder(url_id: str, url_pin: str) -> str:
    cdn_list = ['sdlhivkecdnems06', 'sklktecdnems03', 'sgdccdnems03']
    cdn = cdn_list[0]
    BITRATE = "160"
    track_url = f"https://{cdn}.cdnsrv.jio.com/jiosaavn.cdn.jio.com/{url_pin}/{url_id}_{BITRATE}.mp4"

    return track_url

def get_recoms(query):
    genre = query[: 3]
    idx = int(query[3:])
    result = []
    if genre == 'pop':
        result = recommend_pop(idx)

    elif genre == 'rap':
        result = recommend_rap(idx)

    elif genre == 'roc':
        result = recommend_rock(idx)
    
    elif genre == 'edm':
        result = recommend_edm(idx)

    elif genre == 'ind':
        result = recommend_ind(idx)
    
    return result


def recommend_pop(query):
    BASE_DIR = os.getcwd()
    DB_DIR = "src/database/rezo.db"
    DB_PATH = os.path.join(BASE_DIR, DB_DIR)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    item_list = []
    
    ref_id = "pop" + str(query)
    cur.execute("SELECT album_id FROM tracks_fts4 WHERE ref_id = ?", (ref_id, ))
    album_id = cur.fetchone()[0]
    cur.execute(
                """    
                    SELECT ref_id, track_name, a.album_name, art.artist_name, a.album_img, url_id, url_pin
                    FROM tracks_fts4 t
                    INNER JOIN albums a
                    ON t.album_id = a.album_id
                    INNER JOIN artists art
                    ON a.artist_id = art.artist_id
                    WHERE t.album_id = ?
                    ORDER BY art.artist_popularity DESC
                    LIMIT 10
                """, (album_id, ))
    album_tracks = cur.fetchall()
    if len(album_tracks) >= 4:
        rand_idx = random.sample(range(0, len(album_tracks)), 4)
        for idx in rand_idx:
            if album_tracks[idx][0] == ref_id:
                continue
            
            else:
                url_id = album_tracks[idx][5]
                url_pin = album_tracks[idx][6]
                track_url = track_url_encoder(url_id, url_pin)
                track_dict = {
                "track_id": album_tracks[idx][0],
                "track_name": album_tracks[idx][1],
                "album_name": album_tracks[idx][2],
                "artist_name": album_tracks[idx][3],
                "album_image": album_tracks[idx][4],
                "track_url": track_url
            }
            item_list.append(track_dict)
        
        if len(item_list) == 4:
            item_list = item_list[: 3]
    
    sim = np.load("src/database/pop-light.npy")
    recoms_list = sim[query, :]
    for i in recoms_list:
        idx = 'pop' + str(int(i))
        cur.execute("""
                    SELECT ref_id, track_name, a.album_name, art.artist_name, a.album_img, url_id, url_pin
                    FROM tracks_fts4 t
                    INNER JOIN albums a
                    ON t.album_id = a.album_id
                    INNER JOIN artists art
                    ON a.artist_id = art.artist_id
                    WHERE t.ref_id = ?
                    ORDER BY art.artist_popularity DESC """, (idx, ))
        track = cur.fetchone()
        url_id = track[5]
        url_pin = track[6]
        track_url = track_url_encoder(url_id, url_pin)
        track_dict = {
            "track_id": track[0],
            "track_name": track[1],
            "album_name": track[2],
            "artist_name": track[3],
            "album_image": track[4],
            "track_url": track_url
        }
        item_list.append(track_dict)
    conn.close()
    return item_list


def recommend_rap(query):
    BASE_DIR = os.getcwd()
    DB_DIR = "src/database/rezo.db"
    DB_PATH = os.path.join(BASE_DIR, DB_DIR)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    item_list = []
    
    ref_id = "rap" + str(query)
    cur.execute("SELECT album_id FROM tracks_fts4 WHERE ref_id = ?", (ref_id, ))
    album_id = cur.fetchone()[0]
    cur.execute(
                """    
                    SELECT ref_id, track_name, a.album_name, art.artist_name, a.album_img, url_id, url_pin
                    FROM tracks_fts4 t
                    INNER JOIN albums a
                    ON t.album_id = a.album_id
                    INNER JOIN artists art
                    ON a.artist_id = art.artist_id
                    WHERE t.album_id = ?
                    ORDER BY art.artist_popularity DESC
                    LIMIT 10
                """, (album_id, ))
    album_tracks = cur.fetchall()
    if len(album_tracks) >= 4:
        rand_idx = random.sample(range(0, len(album_tracks)), 4)
        for idx in rand_idx:
            if album_tracks[idx][0] == ref_id:
                continue
            
            else:
                url_id = album_tracks[idx][5]
                url_pin = album_tracks[idx][6]
                track_url = track_url_encoder(url_id, url_pin)
                track_dict = {
                "track_id": album_tracks[idx][0],
                "track_name": album_tracks[idx][1],
                "album_name": album_tracks[idx][2],
                "artist_name": album_tracks[idx][3],
                "album_image": album_tracks[idx][4],
                "track_url": track_url
            }
            item_list.append(track_dict)
        
        if len(item_list) == 4:
            item_list = item_list[: 3]
    
    sim = np.load("src/database/rap-light.npy")
    recoms_list = sim[query, :]
    for i in recoms_list:
        idx = 'rap' + str(int(i))
        cur.execute("""
                    SELECT ref_id, track_name, a.album_name, art.artist_name, a.album_img, url_id, url_pin
                    FROM tracks_fts4 t
                    INNER JOIN albums a
                    ON t.album_id = a.album_id
                    INNER JOIN artists art
                    ON a.artist_id = art.artist_id
                    WHERE t.ref_id = ?
                    ORDER BY art.artist_popularity DESC """, (idx, ))
        track = cur.fetchone()
        url_id = track[5]
        url_pin = track[6]
        track_url = track_url_encoder(url_id, url_pin)
        track_dict = {
            "track_id": track[0],
            "track_name": track[1],
            "album_name": track[2],
            "artist_name": track[3],
            "album_image": track[4],
            "track_url": track_url
        }
        item_list.append(track_dict)
    conn.close()
    return item_list
    

def recommend_edm(query):
    BASE_DIR = os.getcwd()
    DB_DIR = "src/database/rezo.db"
    DB_PATH = os.path.join(BASE_DIR, DB_DIR)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    item_list = []
    
    ref_id = "edm" + str(query)
    cur.execute("SELECT album_id FROM tracks_fts4 WHERE ref_id = ?", (ref_id, ))
    album_id = cur.fetchone()[0]
    cur.execute(
                """    
                    SELECT ref_id, track_name, a.album_name, art.artist_name, a.album_img, url_id, url_pin
                    FROM tracks_fts4 t
                    INNER JOIN albums a
                    ON t.album_id = a.album_id
                    INNER JOIN artists art
                    ON a.artist_id = art.artist_id
                    WHERE t.album_id = ?
                    ORDER BY art.artist_popularity DESC
                    LIMIT 10
                """, (album_id, ))
    album_tracks = cur.fetchall()
    if len(album_tracks) >= 4:
        rand_idx = random.sample(range(0, len(album_tracks)), 4)
        for idx in rand_idx:
            if album_tracks[idx][0] == ref_id:
                continue
            
            else:
                url_id = album_tracks[idx][5]
                url_pin = album_tracks[idx][6]
                track_url = track_url_encoder(url_id, url_pin)
                track_dict = {
                "track_id": album_tracks[idx][0],
                "track_name": album_tracks[idx][1],
                "album_name": album_tracks[idx][2],
                "artist_name": album_tracks[idx][3],
                "album_image": album_tracks[idx][4],
                "track_url": track_url
            }
            item_list.append(track_dict)
        
        if len(item_list) == 4:
            item_list = item_list[: 3]
    
    sim = np.load("src/database/edm-light.npy")
    recoms_list = sim[query, :]
    for i in recoms_list:
        idx = 'edm' + str(int(i))
        cur.execute("""
                    SELECT ref_id, track_name, a.album_name, art.artist_name, a.album_img, url_id, url_pin
                    FROM tracks_fts4 t
                    INNER JOIN albums a
                    ON t.album_id = a.album_id
                    INNER JOIN artists art
                    ON a.artist_id = art.artist_id
                    WHERE t.ref_id = ?
                    ORDER BY art.artist_popularity DESC """, (idx, ))
        track = cur.fetchone()
        url_id = track[5]
        url_pin = track[6]
        track_url = track_url_encoder(url_id, url_pin)
        track_dict = {
            "track_id": track[0],
            "track_name": track[1],
            "album_name": track[2],
            "artist_name": track[3],
            "album_image": track[4],
            "track_url": track_url
        }
        item_list.append(track_dict)
    conn.close()
    return item_list


def recommend_rock(query):
    BASE_DIR = os.getcwd()
    DB_DIR = "src/database/rezo.db"
    DB_PATH = os.path.join(BASE_DIR, DB_DIR)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    item_list = []
    
    ref_id = "roc" + str(query)
    cur.execute("SELECT album_id FROM tracks_fts4 WHERE ref_id = ?", (ref_id, ))
    album_id = cur.fetchone()[0]
    cur.execute(
                """    
                    SELECT ref_id, track_name, a.album_name, art.artist_name, a.album_img, url_id, url_pin
                    FROM tracks_fts4 t
                    INNER JOIN albums a
                    ON t.album_id = a.album_id
                    INNER JOIN artists art
                    ON a.artist_id = art.artist_id
                    WHERE t.album_id = ?
                    ORDER BY art.artist_popularity DESC
                    LIMIT 10
                """, (album_id, ))
    album_tracks = cur.fetchall()
    if len(album_tracks) >= 4:
        rand_idx = random.sample(range(0, len(album_tracks)), 4)
        for idx in rand_idx:
            if album_tracks[idx][0] == ref_id:
                continue
            
            else:
                url_id = album_tracks[idx][5]
                url_pin = album_tracks[idx][6]
                track_url = track_url_encoder(url_id, url_pin)
                track_dict = {
                "track_id": album_tracks[idx][0],
                "track_name": album_tracks[idx][1],
                "album_name": album_tracks[idx][2],
                "artist_name": album_tracks[idx][3],
                "album_image": album_tracks[idx][4],
                "track_url": track_url
            }
            item_list.append(track_dict)
        
        if len(item_list) == 4:
            item_list = item_list[: 3]
    
    sim = np.load("src/database/roc-light.npy")
    recoms_list = sim[query, :]
    for i in recoms_list:
        idx = 'roc' + str(int(i))
        cur.execute("""
                    SELECT ref_id, track_name, a.album_name, art.artist_name, a.album_img, url_id, url_pin
                    FROM tracks_fts4 t
                    INNER JOIN albums a
                    ON t.album_id = a.album_id
                    INNER JOIN artists art
                    ON a.artist_id = art.artist_id
                    WHERE t.ref_id = ?
                    ORDER BY art.artist_popularity DESC """, (idx, ))
        track = cur.fetchone()
        url_id = track[5]
        url_pin = track[6]
        track_url = track_url_encoder(url_id, url_pin)
        track_dict = {
            "track_id": track[0],
            "track_name": track[1],
            "album_name": track[2],
            "artist_name": track[3],
            "album_image": track[4],
            "track_url": track_url
        }
        item_list.append(track_dict)
    conn.close()
    return item_list

    
def recommend_ind(query):
    BASE_DIR = os.getcwd()
    DB_DIR = "src/database/rezo.db"
    DB_PATH = os.path.join(BASE_DIR, DB_DIR)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    item_list = []
    
    ref_id = "ind" + str(query)
    cur.execute("SELECT album_id FROM tracks_fts4 WHERE ref_id = ?", (ref_id, ))
    album_id = cur.fetchone()[0]
    cur.execute(
                """    
                    SELECT ref_id, track_name, a.album_name, art.artist_name, a.album_img, url_id, url_pin
                    FROM tracks_fts4 t
                    INNER JOIN albums a
                    ON t.album_id = a.album_id
                    INNER JOIN artists art
                    ON a.artist_id = art.artist_id
                    WHERE t.album_id = ?
                    ORDER BY art.artist_popularity DESC
                    LIMIT 10
                """, (album_id, ))
    album_tracks = cur.fetchall()
    if len(album_tracks) >= 4:
        rand_idx = random.sample(range(0, len(album_tracks)), 4)
        for idx in rand_idx:
            if album_tracks[idx][0] == ref_id:
                continue
            
            else:
                url_id = album_tracks[idx][5]
                url_pin = album_tracks[idx][6]
                track_url = track_url_encoder(url_id, url_pin)
                track_dict = {
                "track_id": album_tracks[idx][0],
                "track_name": album_tracks[idx][1],
                "album_name": album_tracks[idx][2],
                "artist_name": album_tracks[idx][3],
                "album_image": album_tracks[idx][4],
                "track_url": track_url
            }
            item_list.append(track_dict)
        
        if len(item_list) == 4:
            item_list = item_list[: 3]
    
    sim = np.load("src/database/ind-light.npy")
    recoms_list = sim[query, :]
    for i in recoms_list:
        idx = 'ind' + str(int(i))
        cur.execute("""
                    SELECT ref_id, track_name, a.album_name, art.artist_name, a.album_img, url_id, url_pin
                    FROM tracks_fts4 t
                    INNER JOIN albums a
                    ON t.album_id = a.album_id
                    INNER JOIN artists art
                    ON a.artist_id = art.artist_id
                    WHERE t.ref_id = ?
                    ORDER BY art.artist_popularity DESC """, (idx, ))
        track = cur.fetchone()
        url_id = track[5]
        url_pin = track[6]
        track_url = track_url_encoder(url_id, url_pin)
        track_dict = {
            "track_id": track[0],
            "track_name": track[1],
            "album_name": track[2],
            "artist_name": track[3],
            "album_image": track[4],
            "track_url": track_url
        }
        item_list.append(track_dict)
    conn.close()
    return item_list



