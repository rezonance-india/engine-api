import requests
import json
from . import secret
import redis
import datetime


def fetch_trending():
    redis_client = redis.Redis(host='localhost', port=6379, db=3)
    cached_data = redis_client.get('data')

    if cached_data is not None:
        json_data = json.loads(cached_data)
        return json_data

    else:
        res = requests.get("https://www.jiosaavn.com/featured/now-trending---english/pm49jiq,CNs_").text
        id = res.split('"type":"playlist","id":"')[1].split('"')[0]
        res = requests.get(f"https://www.jiosaavn.com/api.php?__call=playlist.getDetails&_format=json&cc=in&_marker=0%3F_marker%3D0&listid={id}")

        songs_json = res.text.encode().decode('unicode-escape')
        songs_json = json.loads(songs_json)
        songs_list = songs_json['songs']
        
        result_list = []

        for item in songs_list:
            try:
                song_prev_url = item['media_preview_url']
            except Exception as e:
                continue
            
            song_id = song_prev_url.split('/')[3]
            song_url = song_prev_url.split('/')[4].split('_')[0]
            url = f"https://{secret.cdn_list[0]}.{secret.BASE_URL}/{song_id}/{song_url}_96.mp4"

            img_url = item['image']
            img_suffix = "500x500.jpg"
            album_image = img_url[: -11] + img_suffix

            song_dict = {
                "ref_id": "trending",
                "track_name": item['song'],
                "album_name": item['album'],
                "artist_name": item['primary_artists'],
                "album_image": album_image,
                "track_url": url
            }

            result_list.append(song_dict)

        redis_client.setex('data', datetime.timedelta(days=1), json.dumps(result_list))
        return result_list

