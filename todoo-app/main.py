# main.py
from fastapi import FastAPI

app =  FastAPI()
    
# simple get request to test
@app.get("/")
def read_root():
    return {"Hello" : "World"}

# read all todos from the database
@app.get("/city")
def city():
    return {"City" : "Lahore"}
