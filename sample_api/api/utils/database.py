# para crear una base de datos asincrona
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


async def get_db():
    # levantamos la base de datos asincrona
    client = AsyncIOMotorClient(
        # ip del contenedor
        # se tiene que cambiar
        "mongodb://academia:academia@172.17.0.3:27017"
    )
    return client.academia
