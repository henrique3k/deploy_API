import sqlite3, datetime


def inserir_dados(dados):
    print(dados.c)
    global cursor
    try:
        conn = sqlite3.connect('deploy.db')
        cursor = conn.cursor()
    except Exception as e:
        print("Erro ao conectar ao bd.", str(e))
    try:
        cursor.execute(f"""INSERT INTO deploy (componente, versao, responsavel, status, data) VALUES ('{dados.c}',{float(dados.v)}, '{dados.r}', '{dados.s}', '{datetime.datetime.now()}')""")
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Não foi possível salvar os dados", str(e))
        cursor.close()
        return False
