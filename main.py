from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
        },
        {
            'name': 'samuel ariza',
            'email': 'arizasamuel@gmail.com'
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
