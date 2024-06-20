from fastapi import APIRouter,HTTPException
from app.db_connection import connect_db

router = APIRouter()

# GET games by genre and name
@router.get("/action", tags=["Genres"])
def get_game_by_genre_action():

    try:
        conn,cur = connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = "select * from api.game_info where genre ILIKE '%action%' order by game_title ASC"
        cur.execute(sql_query)
        result = cur.fetchall()
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return {"game_info": result}
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()
        
# GET games by genre and name
@router.get("/fps", tags=["Genres"])
def get_game_by_genre_rpg():

    try:
        conn,cur = connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = "select * from api.game_info where genre ILIKE '%fps%' order by game_title ASC"
        cur.execute(sql_query)
        result = cur.fetchall()
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return {"game_info": result}
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()
        
@router.get("/rpg", tags=["Genres"])
def get_game_by_genre_fps():

    try:
        conn,cur = connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = "select * from api.game_info where genre ILIKE '%rpg%' order by game_title ASC"
        cur.execute(sql_query)
        result = cur.fetchall()
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return {"game_info": result}
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()

@router.get("/adventure", tags=["Genres"])
def get_game_by_genre_adventure():

    try:
        conn,cur = connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = "select * from api.game_info where genre ILIKE '%adv%' order by game_title ASC"
        cur.execute(sql_query)
        result = cur.fetchall()
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return {"game_info": result}
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()
        
@router.get("/shooter", tags=["Genres"])
def get_game_by_genre_shooter():

    try:
        conn,cur = connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = "select * from api.game_info where genre ILIKE '%shoot%' order by game_title ASC"
        cur.execute(sql_query)
        result = cur.fetchall()
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return {"game_info": result}
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()


@router.get("/sports", tags=["Genres"])
def get_game_by_genre_sports():

    try:
        conn,cur = connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = "select * from api.game_info where genre ILIKE '%sport%' order by game_title ASC"
        cur.execute(sql_query)
        result = cur.fetchall()
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return {"game_info": result}
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()
    
@router.get("/fighting", tags=["Genres"])
def get_game_by_genre_fighting():

    try:
        conn,cur = connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = "select * from api.game_info where genre ILIKE '%fight%' order by game_title ASC"
        cur.execute(sql_query)
        result = cur.fetchall()
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return {"game_info": result}
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()

@router.get("/survival", tags=["Genres"])
def get_game_by_genre_survival():

    try:
        conn,cur = connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = "select * from api.game_info where genre ILIKE '%surv%' order by game_title ASC"
        cur.execute(sql_query)
        result = cur.fetchall()
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return {"game_info": result}
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()

@router.get("/racing", tags=["Genres"])
def get_game_by_genre_racing():

    try:
        conn,cur = connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = "select * from api.game_info where genre ILIKE '%rac%' order by game_title ASC"
        cur.execute(sql_query)
        result = cur.fetchall()
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return {"game_info": result}
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()
        
@router.get("/puzzle", tags=["Genres"])
def get_game_by_genre_puzzle():

    try:
        conn,cur = connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = "select * from api.game_info where genre ILIKE '%puzz%' order by game_title ASC"
        cur.execute(sql_query)
        result = cur.fetchall()
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return {"game_info": result}
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()

@router.get("/simulation", tags=["Genres"])
def get_game_by_genre_simulation():

    try:
        conn,cur = connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = "select * from api.game_info where genre ILIKE '%sim%' order by game_title ASC"
        cur.execute(sql_query)
        result = cur.fetchall()
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return {"game_info": result}
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()
        
