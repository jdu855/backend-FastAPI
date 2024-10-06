from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() 

class User(BaseModel):
    email: str
    password: str

@app.get("/")
def read_root():
    return {"nombre": "Juan David Rodriguez"}

@app.get("/users")
def list_users():
    return[
        {
            'name': 'juan david rodriguez',
            'email': 'juanrod@gmail.com'
        },
        {
            'name': 'lady sanches',
            'email': 'sancheslady@gmail.com'
        }
    ]

@app.post("/login")
def login(dato: User):
    if(dato.email == 'juan@gmail.com' and dato.password == '1234'):
        return{
            'estado': 'succes',
            'mensaje': 'Datos correctos',
            'data': {
                'user_id': 1
            }
        }
    return{
            'estado':'error',
            'mensaje':'si yaa!'
        }
