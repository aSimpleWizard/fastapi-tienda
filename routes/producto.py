from fastapi import APIRouter
from config.db import conn
from models.producto import productos
from schemas.producto import Producto
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select

producto = APIRouter()


@producto.get("/productos", tags=["Productos"])
def get_productos():
    return conn.execute(productos.select()).fetchall()


@producto.post("/productos", tags=["Productos"])
def create_producto(producto: Producto):
    new_producto = {
        "tipo": producto.tipo,
        "nombre": producto.nombre,
        "precio": producto.precio,
        "cantidad": producto.cantidad,
        "comentario": producto.comentario
    }
    result = conn.execute(productos.insert().values(new_producto))
    return conn.execute(productos.select().where(productos.c.producto_id == result.lastrowid)).first()


@producto.get("/productos/{id}", tags=["Productos"])
def get_producto(id: int):
    return conn.execute(productos.select().where(productos.c.producto_id == id)).first()


@producto.put("/productos/{id}", tags=["Productos"])
def update_user(producto: Producto, id: int):
    conn.execute(
        productos.update()
        .values(tipo=producto.tipo,
                nombre=producto.nombre,
                precio=producto.precio,
                cantidad=producto.cantidad,
                comentario=producto.comentario)
        .where(productos.c.producto_id == id)
    )
    return conn.execute(productos.select().where(productos.c.producto_id == id)).first()

@producto.put("/productos_cantidad/{id}", tags=["Productos"])
def update_user(cantidad: int, id: int):
    conn.execute(
        productos.update()
        .values(cantidad=cantidad)
        .where(productos.c.producto_id == id)
    )
    return conn.execute(productos.select().where(productos.c.producto_id == id)).first()



@producto.delete("/productos/{id}", tags=["Productos"], status_code=HTTP_204_NO_CONTENT)
def delete_producto(id: int):
    conn.execute(productos.delete().where(productos.c.producto_id == id))
    return conn.execute(productos.select().where(productos.c.producto_id == id)).first()
