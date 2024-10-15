from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from core.connection import connection
from models.user import User
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() 
# Habilitar CORS (si tienes un frontend separado)


class User(BaseModel):
    marca: str
    modelo: str
    color: str
    fecha_de_compra: str

class UserLogin(BaseModel):
    email: str
    password: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def root():
    return {"message": "hello world"}

@app.get("/")
def read_root():
    return {"nombre": "Juan David Rodriguez"}

@app.get("/users/mysql") # <-- Cambiamos la ruta para evitar conflicto
async def get_users_from_mysql():
    cursor = connection.cursor(dictionary=True)  # Asegúrate de que 'connection' esté definida
    query = "SELECT * FROM users" 

    try: 
        cursor.execute(query)
        users = cursor.fetchall()
        return users
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al obtener usuarios de MySQL: {err}")
    finally:
        cursor.close()
    

@app.post("/login")
def login(user: UserLogin):
    # Aquí puedes implementar la lógica de autenticación
    if user.email == 'juan@gmail.com' and user.password == '1234':
        return {
            'estado': 'success',
            'mensaje': 'Datos correctos',
            'data': {
                'user_id': 1
            }
        }
    
    raise HTTPException(status_code=400, detail="Credenciales incorrectas")

@app.get("/users")
async def get_users():
    cursor = connection.cursor(dictionary=true)
    query = "SELECT * FROM users"

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
    query = "INSERT INTO users (marca, modelo, color, fecha_de_compra) VALUES (%s, %s, %s, %s)"
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
    query = "UPDATE users SET marca = %s, modelo = %s, color = %s, fecha_de_compra = %s WHERE id = %s"
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
    query = "DELETE FROM users WHERE id = %s"
    values = (id,)

    try:
        cursor.execute(query, values)
        connection.commit()
        return {"message": "Usuario eliminado correctamente"}
    except (mysql.connector.Error, ValueError) as err:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el usuario: {err}")
    finally:
        cursor.close()