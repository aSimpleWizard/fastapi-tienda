from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine


pokes = Table("pokemons", meta,
              Column("id", String(255)),
              Column("nombre", String(255)),
              Column("tipo", String(255)),
              Column("color", String(255)),
              Column("nivel", String(255)),
              Column("img", String(255)),
              Column("comentario", String(255))
              )

meta.create_all(engine)
