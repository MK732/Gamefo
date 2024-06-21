from typing import List
from fastapi import APIRouter,HTTPException
from app.db_connection import connect_db
from app.models.games_model import Game

router = APIRouter()

# GET games by genre and name
@router.get("/genre/action", tags=["Genres"], response_model=List[Game])
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
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()
        
# GET games by genre and name
@router.get("/genre/fps", tags=["Genres"], response_model=List[Game])
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
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()
        
@router.get("/genre/rpg", tags=["Genres"], response_model=List[Game])
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
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()

@router.get("/genre/adventure", tags=["Genres"], response_model=List[Game])
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
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()

@router.get("/genre/shooter", tags=["Genres"], response_model=List[Game])
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
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()


@router.get("/genre/sports", tags=["Genres"], response_model=List[Game])
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
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()
    
@router.get("/genre/fighting", tags=["Genres"], response_model=List[Game])
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
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()

@router.get("/genre/survival", tags=["Genres"], response_model=List[Game])
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
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()

@router.get("/genre/racing", tags=["Genres"], response_model=List[Game])
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
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()
        
@router.get("/genre/puzzle", tags=["Genres"], response_model=List[Game])
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
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()

@router.get("/genre/simulation", tags=["Genres"], response_model=List[Game])
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
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        cur.close()
        conn.close()
        
