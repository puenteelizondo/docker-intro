import os

# para crear una base de datos asincrona
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# creamos las variables de ambiente
# tenemos que pasar las variables de ambiente de docker-compose a aquiiiiiiiiii
MONGO_INITDB_ROOT_USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_INITDB_ROOT_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")


async def get_db():
    # levantamos la base de datos asincrona
    client = AsyncIOMotorClient(
        # lo hacemos de esta manera la f es para concatenar
        #                                                           le pasamos la ip del servicio para que no alla problemas
        f"mongodb://{MONGO_INITDB_ROOT_USERNAME}:{MONGO_INITDB_ROOT_PASSWORD}@db:27017"
    )
    return client.academia
