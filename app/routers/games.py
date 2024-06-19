from fastapi import APIRouter,HTTPException
from app.db_connection import connect_db

router = APIRouter()

# GET request to get games "LIKE" user query
@router.get("/game_name/{query}", tags=["Games"])
def get_game_many_by_query(query: str):
    search_query = f"%{query}%"  
    # Connect to the database
    try: 
        conn,cur = connect_db()
        
    # If connection fails, return an error message
    except:
        return {"Error" : "Connection to database failed!"}

    # Try to get the games that have a name similar to the query
    try:
        if len(query) < 3 :
            raise Exception("Query must be at least 3 characters long!")
        else:
            sql_query = "SELECT * FROM api.game_info WHERE game_title ILIKE %s order by game_title ASC"
            params = (search_query,)
            cur.execute(sql_query, params)
            conn.commit()
            result = cur.fetchall() 
        
        # If no games are found, return an error message
        if not result:
            return {"Error" : "No Games Found!"}
        return {"game_info": result}
    
    # If an error occurs, return the error message
    except Exception as e:
        return {"Error" : str(e)}
    
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