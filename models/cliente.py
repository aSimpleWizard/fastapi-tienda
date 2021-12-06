from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine


clientes = Table("clientes", meta,
                 Column("cliente_id", Integer, primary_key=True),
                 Column("nombre", String(255)),
                 Column("apellido", String(255)),
                 Column("correo", String(255)),
                 Column("documento_identidad", String(255)),
                 Column("telefono", String(255))
                 )

meta.create_all(engine)
