from fastapi import APIRouter
from config.db import conn
from models.factura import facturas
from schemas.factura import Factura
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select

factura = APIRouter()


@factura.get("/facturas", tags=["Facturas"])
def get_facturas():
    return conn.execute(facturas.select()).fetchall()


@factura.post("/facturas", tags=["Facturas"])
def create_factura(factura: Factura):
    new_factura = {
        "fecha": factura.fecha,
        "cliente_id": factura.cliente_id,
        "descripcion": factura.descripcion,
        "subtotal": factura.subtotal,
        "itbis": factura.itbis,
        "total": factura.total
    }
    result = conn.execute(facturas.insert().values(new_factura))
    return conn.execute(facturas.select().where(facturas.c.factura_id == result.lastrowid)).first()


@factura.get("/facturas/{id}", tags=["Facturas"])
def get_factura(id: int):
    return conn.execute(facturas.select().where(facturas.c.factura_id == id)).first()


@factura.put("/facturas/{id}", tags=["Facturas"])
def update_user(factura: Factura, id: int):
    conn.execute(
        facturas.update()
        .values(fecha=factura.fecha,
                cliente_id=factura.cliente_id,
                descripcion=factura.descripcion,
                subtotal=factura.subtotal,
                itbis=factura.itbis,
                total=factura.total)
        .where(facturas.c.factura_id == id)
    )
    return conn.execute(facturas.select().where(facturas.c.factura_id == id)).first()


@factura.delete("/facturas/{id}", tags=["Facturas"], status_code=HTTP_204_NO_CONTENT)
def delete_factura(id: int):
    conn.execute(facturas.delete().where(facturas.c.factura_id == id))
    return conn.execute(facturas.select().where(facturas.c.factura_id == id)).first()
