from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    edad: int