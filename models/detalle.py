from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Float, Integer, String
from config.db import meta, engine


detalles = Table("detalles", meta,
                 Column("detalle_id", Integer, primary_key=True),
                 Column("nombre", String(255)),
                 Column("precio", Float),
                 Column("cantidad", Integer),
                 Column("total", Float),
                 Column("factura_id", Integer)

                 )

meta.create_all(engine)
