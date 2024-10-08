from fastapi import FastAPI, HTTPException
from core.connection import get_connection, close_connection
from models.user import UserCreate, UserUpdate, UserOut
from typing import List

app = FastAPI()

# Habilitar CORS (si tienes un frontend separado)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las solicitudes de cualquier origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Ruta para crear usuario (POST)
@app.post("/users/create", response_model=UserOut)
def create_user(user: UserCreate):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (user.username, user.password))
        connection.commit()

        user_id = cursor.lastrowid
        return {"id": user_id, "username": user.username}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=400, detail="Error al crear usuario")
    finally:
        cursor.close()
        close_connection(connection)


# Ruta para listar usuarios (GET)
@app.get("/users/mysql", response_model=List[UserOut])
def list_users():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT id, username FROM users")
    users = cursor.fetchall()

    cursor.close()
    close_connection(connection)

    return users


# Ruta para actualizar usuario (PUT)
@app.put("/users/update/{user_id}", response_model=UserOut)
def update_user(user_id: int, user: UserUpdate):
    connection = get_connection()
    cursor = connection.cursor()

    fields_to_update = []
    params = []

    if user.username:
        fields_to_update.append("username = %s")
        params.append(user.username)
    
    if user.password:
        fields_to_update.append("password = %s")
        params.append(user.password)
    
    params.append(user_id)
    fields = ", ".join(fields_to_update)

    query = f"UPDATE users SET {fields} WHERE id = %s"

    try:
        cursor.execute(query, tuple(params))
        connection.commit()

        return {"id": user_id, "username": user.username if user.username else "Sin cambios"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=400, detail="Error al actualizar usuario")
    finally:
        cursor.close()
        close_connection(connection)


# Ruta para eliminar usuario (DELETE)
@app.delete("/users/delete/{user_id}")
def delete_user(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        connection.commit()

        return {"message": "Usuario eliminado con éxito"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=400, detail="Error al eliminar usuario")
    finally:
        cursor.close()
        close_connection(connection)
