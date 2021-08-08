import requests
import json



def fetch_trending():
    res = requests.get("https://www.jiosaavn.com/featured/english_chartbusters/1HiqW,xnqZTfemJ68FuXsA__").text
    id = res.split('"type":"playlist","id":"')[1].split('"')[0]


    res = requests.get(f"https://www.jiosaavn.com/api.php?__call=playlist.getDetails&_format=json&cc=in&_marker=0%3F_marker%3D0&listid={id}")

    songs_json = res.text.encode().decode('unicode-escape')
    songs_json = json.loads(songs_json)
    songs_list = songs_json['songs']

    result_list = []

    for item in songs_list:
        song_prev_url = item['media_preview_url']
        song_id = song_prev_url.split('/')[3]
        song_url = song_prev_url.split('/')[4].split('_')[0]
        url = f"http://sdlhivkecdnems06.cdnsrv.jio.com/jiosaavn.cdn.jio.com/{song_id}/{song_url}_96.mp4"

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


    return result_list



