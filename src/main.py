from logging import debug
from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn


app = FastAPI()


class Search(BaseModel):
    query: str

@app.post('/search/tracks')
def search_tracks(request_body: Search) -> dict:
    """search for tracks in database

    Args:
        request_body (Search): Schema of Request Body
    """
    data = request_body.query




if __name__ == "__main__":
    uvicorn.run(app, debug=True)