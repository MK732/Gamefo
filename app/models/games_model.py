from pydantic import BaseModel
from fastapi import FastAPI
from typing import List

class Game(BaseModel):
    id: int
    game_title: str
    release_date: str
    publisher: str
    developer: str
    genre: str
    platforms: List[str]
    
    