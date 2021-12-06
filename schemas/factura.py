from typing import Optional
from pydantic import BaseModel


class Factura(BaseModel):
    factura_id: Optional[int]
    fecha: str
    cliente_id: str
    descripcion: str
    subtotal: float
    itbis: float
    total: float
