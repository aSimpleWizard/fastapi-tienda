from fastapi import FastAPI

from routes.poke import poke

from routes.factura import factura
from routes.cliente import cliente
from routes.detalle import detalle
from routes.producto import producto

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API tienda online",
    description="Es una api de facturas, articulos, clientes y usuarios",
    version="0.0.1",
    openapi_tags=[
        {
            "name": "Facturas",
            "description": "Rutas de Facturas"
        },
        {
            "name": "Detalles",
            "description": "Rutas de Detalle"
        },
        {
            "name": "Clientes",
            "description": "Rutas de Clientes"
        },
        {
            "name": "Productos",
            "description": "Rutas de Productos"
        },

    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.include_router(poke)
app.include_router(factura)
app.include_router(cliente)
app.include_router(detalle)
app.include_router(producto)
