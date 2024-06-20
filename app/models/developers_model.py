from pydantic import BaseModel
from typing import List

from app.models.games_model import Game

class Developer(BaseModel):
    developer: str | None
    games: List[str] | None
    
    