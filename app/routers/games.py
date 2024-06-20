from typing import List
from fastapi import APIRouter,HTTPException,Path
from app.db_connection import connect_db
from app.models.games_model import Game

router = APIRouter()

# GET request to get games "LIKE" user query
@router.get("/game_name/{game_name}", tags=["Games",], response_model=List[Game])
def get_game_many_by_query(game_title: str):
    search_query = f"%{game_title}%"  
    # Connect to the database
    try: 
        conn,cur = connect_db()
        
    # If connection fails, return an error message
    except:
        raise Exception("Connection to database failed!")

    # Try to get the games that have a name similar to the query
    try:
        if len(game_title) < 3 :
            raise Exception("Query must be at least 3 characters long!")
        else:
            sql_query = "SELECT * FROM api.game_info WHERE game_title ILIKE %s order by game_title ASC"
            params = (search_query,)
            cur.execute(sql_query, params)
            result = cur.fetchall() 
            games = []
        # If no games are found, return an error message
        if not result:
            raise Exception("No Games Found!")
        return result
    
    # If an error occurs, return the error message
    except Exception as e:
        return {"Error" : str(e)}
    finally:
        cur.close()
        conn.close()
    
@router.get("/games", tags=["Games"], response_model=List[Game])
def get_all_games():
  
    # Connect to the database
    try: 
        conn,cur = connect_db()
        
    # If connection fails, return an error message
    except:
        return {"Error" : "Connection to database failed!"}

    # Try to get the games that have a name similar to the query
    try:
     
        sql_query = "SELECT * FROM api.game_info order by game_title ASC"
    
        cur.execute(sql_query)
        result = cur.fetchall() 
        
        # If no games are found, return an error message
        if not result:
            return {"Error" : "No Games Found!"}
        return {"game_info": result}
    
    # If an error occurs, return the error message
    except Exception as e:
        return {"Error" : str(e)}
    finally:
        cur.close()
        conn.close()
    

### GET request for games by name and genre, seems redundant
### Will keep it here for now, but may remove it later

# # GET games by genre and name
# @router.get("/gamefo/action/{query}", tags=["games"])
# def get_game_by_action_and_name(query: str):
#     search_query = f"%{query}%"
#     try:
#         conn,cur = connect_db()
#     except:
#         raise HTTPException(status_code=500, detail="Connection to database failed!")
    
#     try:
#         sql_query = "SELECT * FROM api.game_info WHERE genre ILIKE %s AND game_title ILIKE %s"
#         params = ('%Action%', search_query)
#         cur.execute(sql_query, params)
#         conn.commit()
#         result = cur.fetchall()
            
#         if not result:
#            raise HTTPException(status_code=404, detail="No Games Found!")
#         return {"game_info": result}
        
#     except:
#        raise HTTPException(status_code=500, detail="An error occurred!")
#     finally:
#         cur.close()
#         conn.close()
        
        
# @router.get("/gamefo/FPS/{query}", tags=["games"])
# def get_game_by_fps_and_name(query: str):
#     search_query = f"%{query}%"
#     try:
#         conn,cur = connect_db()
#     except:
#         raise HTTPException(status_code=500, detail="Connection to database failed!")
    
#     try:
#         sql_query = "SELECT * FROM api.game_info WHERE genre ILIKE %s AND game_title ILIKE %s"
#         params = ('%FPS%', search_query)
#         cur.execute(sql_query, params)
#         conn.commit()
#         result = cur.fetchall()
            
#         if not result:
#            raise HTTPException(status_code=404, detail="No Games Found!")
#         return {"game_info": result}
        
#     except:
#        raise HTTPException(status_code=500, detail="An error occurred!")
#     finally:
#         cur.close()
#         conn.close()