from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from jose import jwt
from pydantic import BaseModel 
import mysql.connector
from core.connection import connection
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    marca: str
    modelo: str
    color: str
    fecha_de_compra: str
class UserLogin(BaseModel):
    email: str
    password: str

users = {
    "juan": {"username": "juan", "password": "1234", "email": "juan@gmail.com"}
}

def encode_token(payload: dict) -> str:
    token = jwt.encode(payload, key="secret", algorithm="HS256")
    return token

def decode_token(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    try:
        data = jwt.decode(token, key="secret", algorithms=["HS256"])
        return data
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
def login(form_data: UserLogin):
    user = None
    for u in users.values():
        if u["email"] == form_data.email:
            user = u
            break

    if not user or form_data.password != user["password"]:
        raise HTTPException(status_code=404, detail="Incorrect user or password")
    
    token = encode_token({"email": user["email"]})

    return {"access_token": token, "token_type": "bearer"}
@app.get("/users/mysql") 
async def get_users_from_mysql():
    cursor = connection.cursor(dictionary=True)  

    try: 
        cursor.execute(query)
        users = cursor.fetchall()
        return users
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al obtener usuarios de MySQL: {err}")
    finally:
        cursor.close()
    

@app.get("/users")
async def get_users():
    cursor = connection.cursor(dictionary=True) 
    query = "SELECT * FROM cars"  

    try: 
        cursor.execute(query)
        users = cursor.fetchall()
        return users
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al conectar con mysql : {err}")
    finally:
        cursor.close()

@app.post('/user')
async def create_user(user: User):
    cursor = connection.cursor()
    query = "INSERT INTO cars (marca, modelo, color, fecha_de_compra) VALUES (%s, %s, %s, %s)" 
    values = (user.marca, user.modelo, user.color, user.fecha_de_compra)

    try:
        cursor.execute(query, values)
        connection.commit()
        return {"message": "Usuario creado correctamente"}
    except (mysql.connector.Error, ValueError) as err:
        raise HTTPException(status_code=500, detail=f"Error al guardar el usuario: {err}")
    finally:
        cursor.close()


@app.put('/user/{id}')
async def update_user(user: User, id: int):
    cursor = connection.cursor()
    query = "UPDATE cars SET marca = %s, modelo = %s, color = %s, fecha_de_compra = %s WHERE id = %s"  
    values = (user.marca, user.modelo, user.color, user.fecha_de_compra, id)

    try:
        cursor.execute(query, values)
        connection.commit()
        return {"message": "Usuario actualizado correctamente"}
    except (mysql.connector.Error, ValueError) as err:
        raise HTTPException(status_code=500, detail=f"Error al guardar el usuario: {err}")
    finally:
        cursor.close()


@app.delete('/user/{id}')
async def delete_user(id: int):
    cursor = connection.cursor()
    query = "DELETE FROM cars WHERE id = %s" 
    values = (id,)

    try:
        cursor.execute(query, values)
        connection.commit()
        return {"message": "Usuario eliminado correctamente"}
    except (mysql.connector.Error, ValueError) as err:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el usuario: {err}")
    finally:
        cursor.close()