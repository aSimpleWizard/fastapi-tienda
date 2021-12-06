from typing import Optional
from pydantic import BaseModel


class Producto(BaseModel):
    producto_id: Optional[int]
    tipo: str
    nombre: str
    precio: float
    cantidad: int
    comentario: str
