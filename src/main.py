from logging import debug
from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn

import re

from scripts import search

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
    result = search.search_tracks(data)

    return result


@app.post('/search/artists')
def _search_artists(request_body: SearchResource) -> list:
    data = request_body.query
    data = re.sub(r'[^A-Za-z0-9 ]+', '', data)
    result = search.search_artists(data)

    return result


