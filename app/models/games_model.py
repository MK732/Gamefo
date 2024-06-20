from pydantic import BaseModel
from typing import List

class Game(BaseModel):
    id: int
    game_title: str | None
    release_date: str | None
    publisher: str | None
    developer: str | None
    genre: str | None
    platforms: List[str] | None
    
    