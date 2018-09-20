import connect

conn = connect.cria_conexao()
cursor = conn.cursor()


def inserir_dados(componente, versao, responsavel, status, data):
    cursor.execute(f"INSERT INTO deploy VALUES ({componente}, {versao}, {responsavel}, "
                   f"{status}, {data})")
