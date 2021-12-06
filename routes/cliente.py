from fastapi import APIRouter
from config.db import conn
from models.cliente import clientes
from schemas.cliente import Cliente
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select

cliente = APIRouter()


@cliente.get("/clientes", tags=["Clientes"])
def get_clientes():
    return conn.execute(clientes.select()).fetchall()


@cliente.post("/clientes", tags=["Clientes"])
def create_cliente(cliente: Cliente):
    new_cliente = {
        "nombre": cliente.nombre,
        "apellido": cliente.apellido,
        "correo": cliente.correo,
        "documento_identidad": cliente.documento_identidad,
        "telefono": cliente.telefono
    }
    result = conn.execute(clientes.insert().values(new_cliente))
    return conn.execute(clientes.select().where(clientes.c.cliente_id == result.lastrowid)).first()


@cliente.get("/clientes/{id}", tags=["Clientes"])
def get_cliente(id: int):
    return conn.execute(clientes.select().where(clientes.c.cliente_id == id)).first()


@cliente.put("/clientes/{id}", tags=["Clientes"])
def update_user(cliente: Cliente, id: int):
    conn.execute(
        clientes.update()
        .values(nombre=cliente.nombre,
                apellido=cliente.apellido,
                correo=cliente.correo,
                documento_identidad=cliente.documento_identidad,
                telefono=cliente.telefono)
        .where(clientes.c.cliente_id == id)
    )
    return conn.execute(clientes.select().where(clientes.c.cliente_id == id)).first()


@cliente.delete("/clientes/{id}", tags=["Clientes"], status_code=HTTP_204_NO_CONTENT)
def delete_cliente(id: int):
    conn.execute(clientes.delete().where(clientes.c.cliente_id == id))
    return conn.execute(clientes.select().where(clientes.c.cliente_id == id)).first()
