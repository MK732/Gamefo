import logging
from fastapi import HTTPException


async def fetch_as_dict(conn, query: str, *args):
    try:
        records = await conn.fetch(query, *args)
        return [dict(record) for record in records]
    except Exception as e:
        logging.error(f"Failed to execute query: {e}")
        raise HTTPException(status_code=500, detail="Failed to execute query!")
