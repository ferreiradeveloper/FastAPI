from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI() 

# entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [
    User(id=1,name ='Francisco',surname= 'Ferreira',url='ferreira.dev',age=55),
    User(id=2,name ='Peter',surname= 'Ferreira',url='ferreira.dev',age=55),
    User(id=3,name ='Panchito',surname= 'Ferreira',url='ferreira.dev',age=55)

]

@app.get("/usersjson")  
async def usersjson():  
    return [{"name": 'Francisco', "surname": "Ferreira", "url": 'https://petersolutions.net', 'age': 54},
            {"name": 'Juan', "surname": "Ferreira", "url": 'https://petersolutions.dev', 'age': 52},
            {"name": 'Peter', "surname": "Ferreira", "url": 'https://petersolutions.com','age': 54},
            {"name": 'Edward', "surname": "Ferreira", "url": 'https://petersolutions.org','age': 28}
            ]


@app.get("/users")  
async def users():  
    return users_list

#PATH
@app.get("/user/{id}")  
async def user(id: int):
    return searh_user(id)  
    

#QUERY    
@app.get("/userqry/")  
async def userqry(id: int):  
    return searh_user(id) 
    

def searh_user(id: int):
        users = filter(lambda user: user.id == id, users_list)
        try:
            return list(users)[0]
        except:
            return {"error: 'user no found!"}
            