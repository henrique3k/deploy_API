import sqlite3, datetime, logging, pymongo
from DAO.connect import connect

logging.basicConfig(filename='deploy_api.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(funcName)s => %(message)s')


def inserir_dados_mongo(dados):
    db = connect()
    dados["data"] = str(datetime.datetime.now())
    try:
        _id = db.deploy_api.insert_one(dados)
        logging.info("Dados inseridos com sucesso.")
        return True, _id
    except Exception as e:
        logging.exception("Erro ao inserir dados no BD. \n", str(e))
        return False, None


def return_dados():
    pass


