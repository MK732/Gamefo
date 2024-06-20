from fastapi import APIRouter,HTTPException
from app.db_connection import connect_db

router = APIRouter()


@router.get("/platforms/{platform}", tags=["Platforms"])
def get_games_by_platforms(platform: str):
    
    # Connect to the database
    try: 
        conn,cur = connect_db()
        
    # If connection fails, return an error message
    except:
        raise Exception("Connection to database failed!")

    # Try to get the games that have a name similar to the query
    try:
        
        sql_query = "SELECT * FROM api.game_info WHERE %s ILIKE ANY(platforms) order by game_title ASC"
        params = (platform)
        cur.execute(sql_query, (platform,))
        result = cur.fetchall() 
        
        # If no games are found, return an error message
        if not result:
            raise Exception("No Games Found!")
        return {"game_info": result}
    
    # If an error occurs, return the error message
    except Exception as e:
        raise HTTPException (status_code=500, detail=str("Could not find games by platform!"))