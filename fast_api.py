import sqlite3
import pandas as pd
from fastapi import FastAPI

app = FastAPI() # creating the application
# allow requests from port 3000
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
)

def get_db_connection():
    # this is a helper function that opens a connection to our database whenever it's needed. Instead of writing sqlite3.connect(...) every time, we call this function
    conn = sqlite3.connect("ngo_database.db")
    conn.row_factory = sqlite3.Row
    # It tells SQLite to return rows as dictionary-like objects instead of plain tuples, so you can access columns by name like row["city"] instead of row[2]
    return conn

@app.get("/") # this means "when someone visits the homepage URL, run the function below"
def home():
    return {"message": "NGO Data API is running"}


@app.get("/cities")
def get_cities():
    conn = get_db_connection()
    result = pd.read_sql("SELECT * FROM city_summary", conn)
    conn.close()
    return result.to_dict(orient="records") # — converts your dataframe into a list of dictionaries, which FastAPI sends as JSON

@app.get("/programs")
def get_programs():
    conn = get_db_connection()
    result = pd.read_sql("SELECT * FROM program_summary", conn)
    conn.close()
    return result.to_dict(orient="records")

@app.get("/full_table")
def get_full_table():
    conn = get_db_connection()
    result = pd.read_sql("SELECT * FROM ngo_clean", conn)
    conn.close()
    return result.to_dict(orient="records")

from fastapi import HTTPException
@app.get("/cities/{city_name}")
def get_city_data(city_name : str):
    conn = get_db_connection()
    result = pd.read_sql("SELECT * FROM ngo_clean WHERE city = ?",
                         conn,
                         params=[city_name])
    conn.close()

    if result.empty:
        raise HTTPException(status_code=404, detail = f"City '{city_name}' not found")
    return result.to_dict(orient="records")

@app.get("/programs/{program_name}")
def get_program_data(program_name: str):
    conn = get_db_connection()
    result = pd.read_sql("SELECT * FROM ngo_clean WHERE program = ?",
                         conn,
                         params=[program_name])
    conn.close()

    if result.empty:
        raise HTTPException(status_code=404, detail = f"Program '{program_name}' not found")
    return result.to_dict(orient="records")


@app.get("/filter")
def filter_data(city:str = None, program: str = None):
    conn = get_db_connection()
    query = "SELECT * FROM ngo_clean WHERE 1=1"
    params = []

    if city:
        query += " AND city = ?"
        params.append(city)

    if program:
        query += " AND program = ?"
        params.append(program)

    result = pd.read_sql(query, conn, params=params)
    conn.close()
    return result.to_dict(orient="records")



# uvicorn fast_api:app --reload