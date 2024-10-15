from pydantic import BaseModel

class User(BaseModel):
    marca: str
    modelo: str
    color:str
    fecha_de_compra:str