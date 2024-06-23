from typing import List
from fastapi import APIRouter,HTTPException
from app.db_connection import connect_db
from app.models.games_model import Game
from app.utils.fetch_as_dictionary import fetch_as_dict

router = APIRouter()

# GET games by genre and name
@router.get("/genre/action", tags=["Genres"], response_model=List[Game])
async def get_game_by_genre_action():

    try:
        conn = await connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = """
                        SELECT 
                            id, game_title, release_date, publisher, developer, genre, platforms 
                        FROM 
                            api.game_info 
                        WHERE 
                            genre ILIKE '%action%' 
                        ORDER BY 
                            game_title 
                        ASC;
        """
        result = await fetch_as_dict(conn, sql_query)
         
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        
        await conn.close()
        

@router.get("/genre/fps", tags=["Genres"], response_model=List[Game])
async def get_game_by_genre_rpg():

    try:
        conn = await connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = """
                        SELECT 
                            id, game_title, release_date, publisher, developer, genre, platforms 
                        FROM 
                            api.game_info 
                        WHERE 
                            genre ILIKE '%fps%' 
                        ORDER BY 
                            game_title 
                        ASC;
        """
        result = await fetch_as_dict(conn, sql_query)
        
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        
        await conn.close()

@router.get("/genre/rpg", tags=["Genres"], response_model=List[Game])
async def get_game_by_genre_fps():

    try:
        conn = await connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = """
                        SELECT 
                            id, game_title, release_date, publisher, developer, genre, platforms 
                        FROM 
                            api.game_info 
                        WHERE 
                            genre ILIKE '%rpg%' 
                        ORDER BY 
                            game_title 
                        ASC;
        """
        result = await fetch_as_dict(conn, sql_query)
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        
        await conn.close()

@router.get("/genre/adventure", tags=["Genres"], response_model=List[Game])
async def get_game_by_genre_adventure():

    try:
        conn = await connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = """
                        SELECT 
                            id, game_title, release_date, publisher, developer, genre, platforms 
                        FROM 
                            api.game_info 
                        WHERE 
                            genre ILIKE '%adv%' 
                        ORDER BY 
                            game_title 
                        ASC;
        """
        result = await fetch_as_dict(conn, sql_query)
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        
        await conn.close()

@router.get("/genre/shooter", tags=["Genres"], response_model=List[Game])
async def get_game_by_genre_shooter():

    try:
        conn = await connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = """
                        SELECT 
                            id, game_title, release_date, publisher, developer, genre, platforms 
                        FROM 
                            api.game_info 
                        WHERE 
                            genre ILIKE '%shoot%' 
                        ORDER BY 
                            game_title 
                        ASC;
        """
        result = await fetch_as_dict(conn,sql_query)
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        
        await conn.close()


@router.get("/genre/sports", tags=["Genres"], response_model=List[Game])
async def get_game_by_genre_sports():

    try:
        conn = await connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = """
                        SELECT 
                            id, game_title, release_date, publisher, developer, genre, platforms 
                        FROM 
                            api.game_info 
                        WHERE 
                            genre ILIKE '%sport%' 
                        ORDER BY 
                            game_title 
                        ASC;
        """
        result = await fetch_as_dict(conn, sql_query)
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        
        await conn.close()
    
@router.get("/genre/fighting", tags=["Genres"], response_model=List[Game])
async def get_game_by_genre_fighting():

    try:
        conn = await connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query ="""
                        SELECT 
                            id, game_title, release_date, publisher, developer, genre, platforms 
                        FROM 
                            api.game_info 
                        WHERE 
                            genre ILIKE '%fight%' 
                        ORDER BY 
                            game_title 
                        ASC;
        """
        result = await fetch_as_dict(conn, sql_query)
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        
        await conn.close()

@router.get("/genre/survival", tags=["Genres"], response_model=List[Game])
async def get_game_by_genre_survival():

    try:
        conn = await connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = """
                        SELECT 
                            id, game_title, release_date, publisher, developer, genre, platforms 
                        FROM 
                            api.game_info 
                        WHERE 
                            genre ILIKE '%surv%' 
                        ORDER BY 
                            game_title 
                        ASC;
        """
        result = await fetch_as_dict(conn, sql_query)
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        
        await conn.close()

@router.get("/genre/racing", tags=["Genres"], response_model=List[Game])
async def get_game_by_genre_racing():

    try:
        conn = await connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query ="""
                        SELECT 
                            id, game_title, release_date, publisher, developer, genre, platforms 
                        FROM 
                            api.game_info 
                        WHERE 
                            genre ILIKE '%rac%' 
                        ORDER BY 
                            game_title 
                        ASC;
        """
        result = await fetch_as_dict(conn, sql_query)
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        
        await conn.close()
        
@router.get("/genre/puzzle", tags=["Genres"], response_model=List[Game])
async def get_game_by_genre_puzzle():

    try:
        conn = await connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = """
                        SELECT 
                            id, game_title, release_date, publisher, developer, genre, platforms 
                        FROM 
                            api.game_info 
                        WHERE 
                            genre ILIKE '%puzz%' 
                        ORDER BY 
                            game_title 
                        ASC;
        """
        result = await fetch_as_dict(conn, sql_query)
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        
        await conn.close()

@router.get("/genre/simulation", tags=["Genres"], response_model=List[Game])
async def get_game_by_genre_simulation():

    try:
        conn = await connect_db()
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!")
    
    try:
        sql_query = """
                        SELECT 
                            id, game_title, release_date, publisher, developer, genre, platforms 
                        FROM 
                            api.game_info 
                        WHERE 
                            genre ILIKE '%sim%' 
                        ORDER BY 
                            game_title 
                        ASC;
        """
        result = await fetch_as_dict(conn, sql_query)
            
        if not result:
           raise HTTPException(status_code=404, detail="No Games Found!")
        return result
        
    except:
       raise HTTPException(status_code=500, detail="No Games Found!")
    finally:
        
        await conn.close()
        
