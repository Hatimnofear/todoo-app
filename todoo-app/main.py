# main.py
from typing import Optional
from fastapi import FastAPI, HTTPException
from sqlmodel import Field, SQLModel, create_engine , Session
from pydantic import BaseModel
class Todos (SQLModel , table = True):
     id : Optional[int] = Field(default=None , primary_key=True)
     content : str 
     is_complete : bool = Field(default=False) 
     
class User_data(BaseModel):
        content : str 
        is_complete : bool = False

# Database URL
db_url = 'postgresql://todoodb_owner:nG2pC5YHbqOl@ep-damp-dawn-a5bi4nt9.us-east-2.aws.neon.tech/todoodb?sslmode=require'

#Create Engine
create_eng = create_engine(db_url , echo= True )

def create_table():
    SQLModel.metadata.create_all(create_eng)

# # Table Inster Data
# data : Todos = Todos(content="coding")
# #Create Session 
# session = Session(create_eng)
# #Session Add
# session.add(data)
# #Session Commit
# session.commit()
# #Session Close
# session.close()

# #Session Delete
# session.delete(data)
# #Session Commit
# session.commit()
# #Session Close
# session.close()
def insert_data_into_table(content : str):
    with Session (create_eng) as session:
        data : Todos = Todos(content=content)
        #Session Add
        session.add(data)
        #Session Commit
        session.commit()
    
app = FastAPI(
    title="Practice To Doo App"
)
@app.get('/')
def route_root():
    return{"message" : "To-Doo Application"}
    
@app.post('/todos')
def add_todos_route(user : User_data):
    if user.content:
        insert_data_into_table(user.content)
        return{"message" : "ToDoos Add Successfully"}
    else:
        raise HTTPException(status_code=404 , detail="No todoos Found" )
    