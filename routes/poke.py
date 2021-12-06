from fastapi import APIRouter
from config.db import conn
from models.poke import pokes
from schemas.poke import Pokemon
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select

poke = APIRouter()


@poke.get("/pokes", tags=["Pokes"])
def get_pokes():
    return conn.execute(pokes.select()).fetchall()


@poke.post("/pokes", tags=["Pokes"])
def create_poke(pokemon: Pokemon):
    new_poke = {
        "id": pokemon.id,
        "nombre": pokemon.nombre,
        "tipo": pokemon.tipo,
        "color": pokemon.color,
        "nivel": pokemon.nivel,
        "img": pokemon.img,
        "comentario": pokemon.comentario
    }
    result = conn.execute(pokes.insert().values(new_poke))
    return conn.execute(pokes.select().where(pokes.c.id == result.lastrowid)).first()


@poke.get("/pokes/{id}", tags=["Pokes"])
def get_poke(id: str):
    return conn.execute(pokes.select().where(pokes.c.id == id)).first()


@poke.put("/pokes/{id}", tags=["Pokes"])
def update_user(pokemon: Pokemon, id: str):
    conn.execute(
        pokes.update()
        .values(nombre=pokemon.nombre,
                tipo=pokemon.tipo,
                color=pokemon.color,
                nivel=pokemon.nivel,
                img=pokemon.img,
                comentario=pokemon.comentario)
        .where(pokes.c.id == id)
    )
    return conn.execute(pokes.select().where(pokes.c.id == id)).first()


@poke.delete("/pokes/{id}", tags=["Pokes"], status_code=HTTP_204_NO_CONTENT)
def delete_poke(id: str):
    conn.execute(pokes.delete().where(pokes.c.id == id))
    return conn.execute(pokes.select().where(pokes.c.id == id)).first()
