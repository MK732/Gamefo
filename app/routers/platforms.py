from typing import List
from fastapi import APIRouter,HTTPException
from app.db_connection import connect_db
from app.models.games_model import Game
from app.utils.fetch_as_dictionary import fetch_as_dict

router = APIRouter()


@router.get("/platforms/{platform}", tags=["Platforms"], response_model=List[Game] )
async def get_games_by_platforms(platform: str):
    
    # Connect to the database
    try: 
        conn = await connect_db()
        
    # If connection fails, return an error message
    except:
        raise Exception("Connection to database failed!")

    # Try to get the games that have a name similar to the query
    try:
        
        sql_query = "SELECT * FROM api.game_info WHERE $1 ILIKE ANY(platforms) order by game_title ASC"
        result = await fetch_as_dict(conn,sql_query, platform)
        
        # If no games are found, return an error message
        if not result:
            raise Exception("No Games Found!")
        return result
    
    # If an error occurs, return the error message
    except Exception as e:
        raise HTTPException (status_code=500, detail=str("Could not find games by platform!"))
    finally:
        await conn.close()