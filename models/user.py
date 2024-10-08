from pydantic import BaseModel

# Modelo para crear usuarios
class UserCreate(BaseModel):
    username: str
    password: str

# Modelo para actualizar usuarios
class UserUpdate(BaseModel):
    username: str = None
    password: str = None

# Modelo para mostrar usuarios con ID
class UserOut(BaseModel):
    id: int
    username: str
