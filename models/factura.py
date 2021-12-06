from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.db import meta, engine


facturas = Table("facturas", meta,
                 Column("factura_id", Integer, primary_key=True),
                 Column("fecha", String(255)),
                 Column("cliente_id", String(255)),
                 Column("descripcion", String(255)),
                 Column("subtotal", Float),
                 Column("itbis", Float),
                 Column("total", Float)
                 )

meta.create_all(engine)
