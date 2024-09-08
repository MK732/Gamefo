from typing import List
from fastapi import APIRouter,HTTPException,Path
from app.db_connection import connect_db
from app.models.games_model import Game
from app.utils.fetch_as_dictionary import fetch_as_dict


router = APIRouter()

# GET request to get games "LIKE" user query
@router.get("/games/v1/{game_title}", tags=["Games"], response_model=List[Game])
async def get_game_few_by_query(game_title: str):
    search_query = f"%{game_title}%"  
    # Connect to the database
    if len(game_title) < 5 :
        raise HTTPException(status_code=400, detail="Query must be at least 3 characters long!")
    try: 
        conn = await connect_db()
        
    # If connection fails, return an error message
    except:
        raise Exception("Connection to database failed!")

    # Try to get the games that have a name similar to the query
    
    try:
        sql_query = """
                        SELECT 
                            id, game_title, release_date, publisher, developer, genre, platforms 
                        FROM 
                            api.game_info 
                        WHERE 
                            game_title ILIKE $1 
                        ORDER BY game_title 
                        ASC;
                    """
        params = (search_query,)
        result = await fetch_as_dict(conn, sql_query, search_query)
        
        
        # If no games are found, return an error message
        if not result:
            raise HTTPException(status_code=404, detail="No Games Found!")
        return result
    
    # If an error occurs, return the error message
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
      
        await conn.close()
@router.get("/games/v2/{game_title}", tags=["Games"], response_model=List[Game])
async def get_game_many_by_query(game_title: str):
    search_query = f"%{game_title}%"  
    # Connect to the database
    if len(game_title) < 3 :
        raise HTTPException(status_code=400, detail="Query must be at least 3 characters long!")
    try: 
        conn = await connect_db()
        
    # If connection fails, return an error message
    except:
        raise Exception("Connection to database failed!")

    # Try to get the games that have a name similar to the query
    
    try:
        sql_query = """
                        SELECT 
                            id, game_title, release_date, publisher, developer, genre, platforms 
                        FROM 
                            api.game_info 
                        WHERE 
                            game_title ILIKE $1 
                        ORDER BY 
                            game_title 
                        ASC;
                    """
        params = (search_query,)
        result = await fetch_as_dict(conn, sql_query, search_query)
        
        
        # If no games are found, return an error message
        if not result:
            raise HTTPException(status_code=404, detail="No Games Found!")
        return result
    
    # If an error occurs, return the error message
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
      
        await conn.close()
    
@router.get("/games", tags=["Games"], response_model=List[Game])
async def get_all_games():
  
    # Connect to the database
    try: 
        conn = await connect_db()
        
    # If connection fails, return an error message
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    # Try to get the games that have a name similar to the query
    try:
     
        sql_query = """ SELECT
                            id, game_title, release_date, publisher, developer, genre, platforms
                        FROM 
                            api.game_info
                        ORDER BY 
                            game_title 
                        ASC"""

        result = await fetch_as_dict(conn, sql_query)
         
        # If no games are found, return an error message
        if not result:
            raise HTTPException(status_code=404, detail="No Games Found!")
        
        return result
    
    # If an error occurs, return the error message
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=f"Error has occured: {str(e)}")
    finally:
        await conn.close()
    

