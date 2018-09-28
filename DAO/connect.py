import pymongo
from pymongo import MongoClient
import os, logging

logging.basicConfig(filename='deploy_api.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(funcName)s => %(message)s')


def connect():
    try:
        client = MongoClient(
            os.environ['DB_PORT_27017_TCP_ADDR'],
            27017)
        #client = MongoClient('mongodb://localhost:27017/')
        db = client.deploy_api
        logging.info("Conexão ao Banco de dados efetuada com sucesso.")
        return db
    except Exception as e:
        logging.exception("Erro ao conectar no MongoDb.", str(e))
