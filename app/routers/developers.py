from fastapi import APIRouter,HTTPException
from app.db_connection import connect_db

router = APIRouter()





@router.get("/developers", tags=["Developers"])
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
        return {"game_info": result}
        
    except:
       raise HTTPException(status_code=500, detail="An error occurred!")
    finally:
        cur.close()
        conn.close()
        
@router.get("/developers/{name}", tags=["Developers"])
def get_games_by_developers_name(name: str):
    search_query = f"%{name}%"
    try:
        conn,cur = connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        if len(name) < 3 :
            raise Exception("Query must be at least 3 characters long!")
        else:
            sql_query = "SELECT developer, ARRAY_AGG(game_title) AS games FROM api.game_info where developer ILIKE %s GROUP BY developer ORDER BY developer ASC"
            params = (search_query)
            cur.execute(sql_query, (search_query,))
            conn.commit()
            result = cur.fetchall()
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return {"game_info": result}
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()