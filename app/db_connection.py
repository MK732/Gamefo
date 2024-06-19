import psycopg2
import os
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv(dotenv_path="/code/app/.env")
# Function to connect to the database
def connect():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        dbname=os.getenv("POSTGRES_DATABASE"),
        user=os.getenv("POSTGRES_USER"),
        password=str(os.getenv("POST_PASSWORD"))
    
    )
    return conn

# Function to create a cursor
def cursor():
    conn = connect()
    # Cursor factory is used to return the result in a dictionary format  
    return conn.cursor(cursor_factory=RealDictCursor) 

def connect_db():
    conn = connect()
    cur = cursor()
    return conn, cur