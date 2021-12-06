from typing import Optional
from pydantic import BaseModel


class Detalle(BaseModel):
    detalle_id: Optional[int]
    nombre: str
    precio: float
    cantidad: int
    total: float
    factura_id: int
