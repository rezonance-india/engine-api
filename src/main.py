from logging import debug
from fastapi import FastAPI
from pydantic import BaseModel

import re

from scripts import search, recommend, fetch


app = FastAPI()


class SearchResource(BaseModel):
    query: str

@app.post('/search/tracks')
def _search_tracks(request_body: SearchResource) -> list:
    """search for tracks in database

    Args:
        request_body (Search): Schema of Request Body
    """
    data = request_body.query
    data = re.sub(r'[^A-Za-z0-9 ]+', '', data)
    result = search.search_tracks(data)

    return result


@app.post('/search/albums')
def _search_albums(request_body: SearchResource) -> list:
    data = request_body.query
    data = re.sub(r'[^A-Za-z0-9 ]+', '', data)
    result = search.search_albums(data)

    return result


@app.post('/search/artists')
def _search_artists(request_body: SearchResource) -> list:
    data = request_body.query
    data = re.sub(r'[^A-Za-z0-9 ]+', '', data)
    result = search.search_artists(data)

    return result


class RecommendResource(BaseModel):
    ref_id: str

@app.post("/recommend")
def _recommendaton(request_body: RecommendResource) -> list:
    ref_id = request_body.ref_id    
    results = recommend.get_recoms(ref_id)

    return results


class FetchTracks(BaseModel):
    album_id: str

@app.post('/fetch/tracks')
def _fetch_tracks(request_body: FetchTracks):
    album_id = request_body.album_id
    results = fetch.albums_tracks(album_id)

    return results


class FetchAlbums(BaseModel):
    artist_id: str

@app.post("/fetch/albums")
def _fetch_albums(request_body: FetchAlbums):
    artist_id = request_body.artist_id
    results = fetch.artist_albums(artist_id)

    return results



