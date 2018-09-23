import sqlite3, datetime, logging

logging.basicConfig(filename='deploy_api.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(funcName)s => %(message)s')


def inserir_dados(dados):
    print(dados.c)
    global cursor
    try:
        conn = sqlite3.connect('deploy.db')
        cursor = conn.cursor()
    except Exception as e:
        logging.info("Erro ao conectar ao bd.")
        logging.exception(str(e))
    try:
        cursor.execute(f"""INSERT INTO deploy (componente, versao, responsavel, status, data) VALUES ('{dados.c}',{float(dados.v)}, '{dados.r}', '{dados.s}', '{datetime.datetime.now()}')""")
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        logging.info("Não foi possível salvar os dados")
        logging.exception(str(e))
        cursor.close()
        return False
