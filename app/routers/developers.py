from typing import List
from fastapi import APIRouter,HTTPException
from app.db_connection import connect_db, fetch_as_dict
from app.models.developers_model import Developer

router = APIRouter()





@router.get("/developers", tags=["Developers"], response_model=List[Developer])
async def get_games_by_developers():

    try:
        conn = await connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = "SELECT developer, ARRAY_AGG(game_title) AS games FROM api.game_info GROUP BY developer ORDER BY developer ASC"
        result = await fetch_as_dict(conn,sql_query)
    
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return result
        
    except:
       raise HTTPException(status_code=500, detail="An error occurred!")
    finally:
        
        await conn.close()
        
@router.get("/developers/{name}", tags=["Developers"], response_model=List[Developer])
async def get_games_by_developers_name(name: str):
    search_query = f"%{name}%"
    
    if len(name) < 3 :
        raise HTTPException(status_code=404, detail="Query must be at least 3 characters long!")
    try:
        conn = await connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = "SELECT developer, ARRAY_AGG(game_title) AS games FROM api.game_info where developer ILIKE $1 GROUP BY developer ORDER BY developer ASC"
        result = await fetch_as_dict(conn, sql_query, search_query)
      
            
        if not result:
           raise HTTPException(status_code=404, detail="No Developers Found!")
       
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Developers Found!")
    finally:
        
        await conn.close()