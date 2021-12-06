from typing import Optional
from pydantic import BaseModel


class Cliente(BaseModel):
    cliente_id: Optional[int]
    nombre: str
    apellido: str
    correo: str
    documento_identidad: str
    telefono: str
