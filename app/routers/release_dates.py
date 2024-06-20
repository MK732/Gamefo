from fastapi import APIRouter,HTTPException
from app.db_connection import connect_db

router = APIRouter()

@router.get("/release_date", tags=["Release Date"])
def get_all_games_by_release_date():
  
    # Connect to the database
    try: 
        conn,cur = connect_db()
        
    # If connection fails, return an error message
    except:
        return {"Error" : "Connection to database failed!"}

    # Try to get the games that have a name similar to the query
    try:
     
        sql_query = "SELECT * FROM api.game_info ORDER BY TO_DATE(release_date, 'MM-DD-YYYY') ASC"
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