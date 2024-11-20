from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from jose import jwt, JWTError
from pydantic import BaseModel
import mysql.connector
from core.connection import connection
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
import uvicorn
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Usar el puerto proporcionado por Render
    uvicorn.run(app, host="0.0.0.0", port=port)


# Crear la aplicación FastAPI
app = FastAPI()

# Middleware para permitir solicitudes CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las direcciones
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Esquema de seguridad OAuth2 con flujo de contraseña
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Modelo de datos para la autenticación
class UserLogin(BaseModel):
    email: str
    password: str

# Simulación de usuarios en memoria (en una aplicación real, esto debería ir en una base de datos)
users = {
    "juan@gmail.com": {"username": "juan@gmail.com", "password": "1234", "email": "juan@gmail.com"}
}

# Función para generar el token JWT
def encode_token(payload: dict) -> str:
    expiration = datetime.utcnow() + timedelta(hours=1)  # El token expira en 1 hora
    payload.update({"exp": expiration})
    token = jwt.encode(payload, key="secret", algorithm="HS256")
    return token

# Función para decodificar el token JWT
def decode_token(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    try:
        data = jwt.decode(token, key="secret", algorithms=["HS256"])
        return data
    except JWTError:
        raise HTTPException(status_code=403, detail="Token inválido o expirado")
    except Exception as e:
        raise HTTPException(status_code=401, detail="Token no válido")

# Ruta para login y generación de token JWT
@app.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    # Buscar el usuario en la base de datos simulada
    user = users.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")

    # Generar el token JWT
    token = encode_token({"sub": user["username"], "email": user["email"]})
    return {"access_token": token, "token_type": "bearer"}

# Ruta para obtener el perfil del usuario (requiere autenticación)
@app.get("/users/profile")
def profile(my_user: Annotated[dict, Depends(decode_token)]):
    # Devuelve los datos del usuario autenticado
    return {"profile": my_user}

# Ruta para obtener usuarios desde MySQL (requiere autenticación)
@app.get("/users/mysql")
async def get_users_from_mysql(current_user: Annotated[dict, Depends(decode_token)]):
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM users"
    try:
        cursor.execute(query)
        users = cursor.fetchall()
        return users
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al obtener usuarios de MySQL: {err}")
    finally:
        cursor.close()

# Ruta para obtener la lista de usuarios (requiere autenticación)
@app.get("/users")
async def get_users(current_user: Annotated[dict, Depends(decode_token)]):
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM users"
    try:
        cursor.execute(query)
        users = cursor.fetchall()
        return users
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al obtener usuarios: {err}")
    finally:
        cursor.close()

# Ruta para crear un usuario (requiere autenticación)
@app.post("/user")
async def create_user(user: UserLogin, current_user: Annotated[dict, Depends(decode_token)]):
    cursor = connection.cursor()
    query = "INSERT INTO users (email, password) VALUES (%s, %s)"
    values = (user.email, user.password)

    try:
        cursor.execute(query, values)
        connection.commit()
        return {"message": "Usuario creado correctamente"}
    except (mysql.connector.Error, ValueError) as err:
        raise HTTPException(status_code=500, detail=f"Error al guardar el usuario: {err}")
    finally:
        cursor.close()

# Ruta para actualizar un usuario (requiere autenticación)
@app.put("/user/{id}")
async def update_user(user: UserLogin, id: int, current_user: Annotated[dict, Depends(decode_token)]):
    cursor = connection.cursor()
    query = "UPDATE users SET email = %s, password = %s WHERE id = %s"
    values = (user.email, user.password, id)

    try:
        cursor.execute(query, values)
        connection.commit()
        return {"message": "Usuario actualizado correctamente"}
    except (mysql.connector.Error, ValueError) as err:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el usuario: {err}")
    finally:
        cursor.close()

# Ruta para eliminar un usuario (requiere autenticación)
@app.delete("/user/{id}")
async def delete_user(id: int, current_user: Annotated[dict, Depends(decode_token)]):
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
