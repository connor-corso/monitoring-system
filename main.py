#!/usr/bin/python3

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from sql_app import crud, models
from sql_app.database import SessionLocal, engine


# database dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
        

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



#####################################################################
## data entry methods

@app.post("/create-dataentry/")
async def create_dataentry():
    pass

@app.get("/get-dataentry/")
async def get_dataentry():
    pass

@app.get("/get-dataentries/")
async def get_dataentries():
    pass


#####################################################################
## data station methods

@app.post("/create-station/")
async def create_station():
    pass

@app.get("/get-station/")
async def get_station():
    pass

@app.get("/get-stations/")
async def get_stations():
    pass


#####################################################################
## data grouping methods

@app.post("/create-grouping/")
async def create_grouping():
    pass

@app.get("/get-grouping/")
async def get_grouping():
    pass

@app.get("/get-groupings/")
async def get_groupings():
    pass

@app.post("/bind-station-to-grouping/")
async def bind_station_to_grouping():
    pass

@app.post("/remove-station-from-grouping/")
async def remove_station_from_grouping():
    pass


