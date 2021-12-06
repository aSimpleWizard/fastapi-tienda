from fastapi import APIRouter
from config.db import conn
from models.detalle import detalles
from schemas.detalle import Detalle
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select

detalle = APIRouter()


@detalle.get("/detalles", tags=["Detalles"])
def get_detalles():
    return conn.execute(detalles.select()).fetchall()


@detalle.post("/detalles", tags=["Detalles"])
def create_detalle(detalle: Detalle):
    new_detalle = {
        "nombre": detalle.nombre,
        "precio": detalle.precio,
        "cantidad": detalle.cantidad,
        "total": detalle.total,
        "factura_id": detalle.factura_id
    }
    result = conn.execute(detalles.insert().values(new_detalle))
    return conn.execute(detalles.select().where(detalles.c.detalle_id == result.lastrowid)).first()


@detalle.get("/detalles/{id}", tags=["Detalles"])
def get_detalle(id: int):
    return conn.execute(detalles.select().where(detalles.c.factura_id == id)).fetchall()


@detalle.put("/detalles/{id}", tags=["Detalles"])
def update_user(detalle: Detalle, id: int):
    conn.execute(
        detalles.update()
        .values(nombre=detalle.nombre,
                precio=detalle.precio,
                cantidad=detalle.cantidad,
                total=detalle.total,
                factura_id=detalle.factura_id)
        .where(detalles.c.detalle_id == id)
    )
    return conn.execute(detalles.select().where(detalles.c.detalle_id == id)).first()


@detalle.delete("/detalles/{id}", tags=["Detalles"], status_code=HTTP_204_NO_CONTENT)
def delete_detalle(id: int):
    conn.execute(detalles.delete().where(detalles.c.detalle_id == id))
    return conn.execute(detalles.select().where(detalles.c.detalle_id == id)).first()
