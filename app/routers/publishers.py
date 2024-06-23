from typing import List
from fastapi import APIRouter,HTTPException
from app.db_connection import connect_db
from app.models.publisher_model import Publisher
from app.utils.fetch_as_dictionary import fetch_as_dict

router = APIRouter()





@router.get("/publishers", tags=["Publishers"], response_model=List[Publisher])
async def get_games_by_publisher():

    try:
        conn = await connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = """SELECT 
                            publisher, ARRAY_AGG(game_title) 
                        AS 
                            games 
                        FROM 
                            api.game_info 
                        GROUP BY 
                            publisher 
                        ORDER BY 
                            publisher 
                        ASC"""
        result = await fetch_as_dict(conn,sql_query)
            
        if not result:
           raise HTTPException(status_code=404, detail="No Publishers Found!")
       
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Publishers Found!")
    finally:
        await conn.close()
        
@router.get("/publishers/{name}", tags=["Publishers"], response_model=List[Publisher])
async def get_games_by_publisher_name(name:str):
    search_query = f"%{name}%"
    
    if len(name) < 3 :
            raise HTTPException(status_code=404,detail="Query must be at least 3 characters long!")
    try:
        conn = await connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = """SELECT 
                            publisher, ARRAY_AGG(game_title) 
                        AS 
                            games 
                        FROM 
                            api.game_info 
                        WHERE 
                            publisher ILIKE $1 
                        GROUP BY 
                            publisher 
                        ORDER BY 
                            publisher 
                        ASC"""
        result = await fetch_as_dict(conn,sql_query, search_query)
        
        return result 
    except:
        raise HTTPException(status_code=404, detail="No Publishers Found!")
    finally:
        await conn.close()