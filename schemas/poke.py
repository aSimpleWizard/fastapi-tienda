from pydantic import BaseModel


class Pokemon(BaseModel):
    id: str
    nombre: str
    tipo: str
    color: str
    nivel: str
    img: str
    comentario: str
