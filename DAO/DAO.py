import sqlite3, datetime, logging, pymongo

import json

from DAO.connect import connect

logging.basicConfig(filename='deploy_api.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(funcName)s => %(message)s')

db = connect()


def inserir_dados_mongo(dados):
    dados["data"] = str(datetime.datetime.now())
    dados_mongo = {"componente": dados.c, "versao": dados.v, "recurso": dados.r, "status": dados.s, "data": dados.data}
    try:
        _id = db.deploy_api.insert_one(dados_mongo)
        logging.info("Dados inseridos com sucesso.")
        return True, _id
    except Exception as e:
        logging.exception("Erro ao inserir dados no BD. \n", str(e))
        return False, None


def return_dados():
    _result = db.deploy_api.find()
    _ret = []
    for item in _result:
        _ret.append(item)
    return _ret






