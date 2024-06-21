import logging
from fastapi import HTTPException
import psycopg2
import os
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import asyncpg

load_dotenv(dotenv_path="/code/app/.env")
# Function to connect to the database
async def connect():
    
    conn =  await asyncpg.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DATABASE"),
        user=os.getenv("POSTGRES_USER"),
        password=str(os.getenv("POSTGRES_PASSWORD")),
        port=os.getenv("POSTGRES_PORT")
    
    )
    return conn

# Function to get connection and cursor (if needed)
async def connect_db():
    conn = await connect()
    try:
        # In asyncpg, you usually work directly with the connection
        # and use its methods for queries instead of creating a cursor
        return conn
    except Exception as e:
        logging.error(f"Error while getting database connection: {e}")
        raise HTTPException(status_code=500, detail="Error while getting database connection!")
    

async def fetch_as_dict(conn, query: str, *args):
    try:
        records = await conn.fetch(query, *args)
        return [dict(record) for record in records]
    except Exception as e:
        logging.error(f"Failed to execute query: {e}")
        raise HTTPException(status_code=500, detail="Failed to execute query!")
