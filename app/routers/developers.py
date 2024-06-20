from typing import List
from fastapi import APIRouter,HTTPException
from app.db_connection import connect_db
from app.models.developers_model import Developer

router = APIRouter()





@router.get("/developers", tags=["Developers"], response_model=List[Developer])
def get_games_by_developers():

    try:
        conn,cur = connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = "SELECT developer, ARRAY_AGG(game_title) AS games FROM api.game_info GROUP BY developer ORDER BY developer ASC"
        cur.execute(sql_query)
        conn.commit()
        result = cur.fetchall()
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return result
        
    except:
       raise HTTPException(status_code=500, detail="An error occurred!")
    finally:
        cur.close()
        conn.close()
        
@router.get("/developers/{name}", tags=["Developers"], response_model=List[Developer])
def get_games_by_developers_name(name: str):
    search_query = f"%{name}%"
    
    if len(name) < 3 :
        raise HTTPException(status_code=404, detail="Query must be at least 3 characters long!")
    try:
        conn,cur = connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = "SELECT developer, ARRAY_AGG(game_title) AS games FROM api.game_info where developer ILIKE %s GROUP BY developer ORDER BY developer ASC"
        params = (search_query)
        cur.execute(sql_query, (search_query,))
        conn.commit()
        result = cur.fetchall()
            
        if not result:
           raise HTTPException(status_code=404, detail="No Developers Found!")
       
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Developers Found!")
    finally:
        cur.close()
        conn.close()