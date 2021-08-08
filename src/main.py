from logging import debug
from typing import Optional
from fastapi import FastAPI, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import re

from scripts import search, recommend, fetch, trending


app = FastAPI()


origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SearchResource(BaseModel):
    query: str

@app.post('/search/tracks')
def _search_tracks(request_body: SearchResource, request: Request) -> list:
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


@app.get('/trending/tracks')
def _fetch_trending():
    trending_tracks = trending.fetch_trending()
    return trending_tracks
    