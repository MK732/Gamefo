from fastapi import APIRouter,HTTPException
from app.db_connection import connect_db, fetch_as_dict

router = APIRouter()

@router.get("/release_date", tags=["Release Date"])
async def get_all_games_by_release_date():
  
    # Connect to the database
    try: 
        conn = await connect_db()
        
    # If connection fails, return an error message
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!") 

    # Try to get the games that have a name similar to the query
    try:
     
        sql_query = "SELECT * FROM api.game_info ORDER BY TO_DATE(release_date, 'MM-DD-YYYY') ASC"
        result = await fetch_as_dict(conn,sql_query)
        
        # If no games are found, return an error message
        if not result:
            raise HTTPException(status_code=404, detail="No Games Found!")
        return {"game_info": result}
    
    # If an error occurs, return the error message
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error has occured")
    finally:
        await conn.close()
        
@router.get("/release_date/{year}", tags=["Release Date"])
async def get_game_by_release_date_by_year(year: str):
    # Grab release date from a range of years
    try: 
        conn = await connect_db()
        
    # If connection fails, return an error message
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!") 

    # Try to get the games that have a name similar to the query
    try:
     
        sql_query = " SELECT * FROM api.game_info WHERE EXTRACT(YEAR FROM TO_DATE(release_date, 'MM-DD-YYYY')) = $1 ORDER BY TO_DATE(release_date, 'MM-DD-YYYY') ASC" 
        result = await fetch_as_dict(conn,sql_query, year)
        
        # If no games are found, return an error message
        if not result:
            raise HTTPException(status_code=404, detail="No Games Found!")
        return {"game_info": result}
    
    # If an error occurs, return the error message
    except Exception as e:
        raise HTTPException(status_code=500, detail=" No Games Found!")
    finally:
        await conn.close()
            
        
        
@router.get("/release_date/{year1}/{year2}", tags=["Release Date"])
async def get_game_by_release_date_by_range(year1: str, year2: str):
    # Grab release date from a range of years
    try: 
        conn = await connect_db()
        
    # If connection fails, return an error message
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!") 

    # Try to get the games that have a name similar to the query
    try:
     
        sql_query = " SELECT *  FROM api.game_info WHERE EXTRACT(YEAR FROM TO_DATE(release_date, 'MM-DD-YYYY')) BETWEEN $1 AND $2 ORDER BY TO_DATE(release_date, 'MM-DD-YYYY') ASC" 
        result = await fetch_as_dict(conn,sql_query, year1,year2)
        
        
        # If no games are found, return an error message
        if not result:
             raise HTTPException(status_code=500, detail="No Games Found!")
        return {"game_info": result}
    
    # If an error occurs, return the error message
    except Exception as e:
        return {"Error" : str(e)}
    finally:
        await conn.close()
    
        
