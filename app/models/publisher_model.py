from pydantic import BaseModel
from typing import List

from app.models.games_model import Game

class Publisher(BaseModel):
    publisher: str | None
    games: List[str] | None
    
    