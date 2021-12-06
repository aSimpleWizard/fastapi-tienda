from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Float, Integer, String
from config.db import meta, engine


productos = Table("productos", meta,
                  Column("producto_id", Integer, primary_key=True),
                  Column("tipo", String(255)),
                  Column("nombre", String(255)),
                  Column("precio", Float),
                  Column("cantidad", Integer),
                  Column("comentario", String(255))
                  )

meta.create_all(engine)
