from fastapi.param_functions import Query
from fastapi.testclient import TestClient

from main import app

import logging


client = TestClient(app)
logger = logging.getLogger()


def test_search_tracks():
    body = {
        "query": "everything has changed"
    }

    response = client.post('/search/tracks', json=body)
    assert response.status_code == 200
    


def test_album_search():
    body = {
       "query": "Red (Big Machine Radio Release Special) Taylor Swift"
    }

    response = client.post('/search/albums', json=body)
    assert response.status_code == 200
    


def test_artist_search():
    body = {
        "query": "taylor swift"
    }
    
    response = client.post('/search/artists', json=body)
    assert response.status_code == 200



def test_recommendation():
    pop_query = {
        "ref_id": "pop120"
    }
    rap_query = {
        "ref_id": "rap120"
    }
    roc_query = {
        "ref_id": "roc120"
    }
    edm_query = {
        "ref_id": "edm120"
    }
    ind_query = {
        "ref_id": "ind120"
    }

    response = client.post("/recommend", json=pop_query)
    assert response.status_code == 200
    response = client.post("/recommend", json=rap_query)
    assert response.status_code == 200
    response = client.post("/recommend", json=roc_query)
    assert response.status_code == 200
    response = client.post("/recommend", json=edm_query)
    assert response.status_code == 200
    response = client.post("/recommend", json=ind_query)
    assert response.status_code == 200


def test_fetch_tracks():
    data = {
        "album_id": "34OkZVpuzBa9y40DCy0LPR"
    }

    response = client.post("/fetch/tracks", json=data)
    assert response.status_code == 200


def test_fetch_albums():
    data = {
        "artist_id": "6qqNVTkY8uBg9cP3Jd7DAH"
    }

    response = client.post("/fetch/albums", json=data)
    assert response.status_code == 200

