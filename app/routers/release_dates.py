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
        raise HTTPException(status_code=500, detail="Connection to database failed!") 

    # Try to get the games that have a name similar to the query
    try:
     
        sql_query = "SELECT * FROM api.game_info ORDER BY TO_DATE(release_date, 'MM-DD-YYYY') ASC"
        cur.execute(sql_query)
        result = cur.fetchall() 
        
        # If no games are found, return an error message
        if not result:
            raise HTTPException(status_code=404, detail="No Games Found!")
        return {"game_info": result}
    
    # If an error occurs, return the error message
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error has occured")
    finally:
        cur.close()
        conn.close()
        
@router.get("/release_date/{year}", tags=["Release Date"])
def get_game_by_release_date_by_year(year: str):
    # Grab release date from a range of years
    try: 
        conn,cur = connect_db()
        
    # If connection fails, return an error message
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!") 

    # Try to get the games that have a name similar to the query
    try:
     
        sql_query = " SELECT * FROM api.game_info WHERE EXTRACT(YEAR FROM TO_DATE(release_date, 'MM-DD-YYYY')) = %s ORDER BY TO_DATE(release_date, 'MM-DD-YYYY') ASC" 
        params = (year)
        cur.execute(sql_query, (params,))
        result = cur.fetchall() 
        
        # If no games are found, return an error message
        if not result:
            raise HTTPException(status_code=404, detail="No Games Found!")
        return {"game_info": result}
    
    # If an error occurs, return the error message
    except Exception as e:
        raise HTTPException(status_code=500, detail=" No Games Found!")
    finally:
        cur.close()
        conn.close()
            
        
        
@router.get("/release_date/{year1}/{year2}", tags=["Release Date"])
def get_game_by_release_date_by_range(year1: str, year2: str):
    # Grab release date from a range of years
    try: 
        conn,cur = connect_db()
        
    # If connection fails, return an error message
    except:
        raise HTTPException(status_code=500, detail="Connection to database failed!") 

    # Try to get the games that have a name similar to the query
    try:
     
        sql_query = " SELECT *  FROM api.game_info WHERE EXTRACT(YEAR FROM TO_DATE(release_date, 'MM-DD-YYYY')) BETWEEN %s AND %s ORDER BY TO_DATE(release_date, 'MM-DD-YYYY') ASC" 
        params = (year1, year2)
        cur.execute(sql_query, params)
        result = cur.fetchall() 
        
        # If no games are found, return an error message
        if not result:
             raise HTTPException(status_code=500, detail="No Games Found!")
        return {"game_info": result}
    
    # If an error occurs, return the error message
    except Exception as e:
        return {"Error" : str(e)}
    finally:
        cur.close()
        conn.close()
    
        
