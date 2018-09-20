import sqlite3


def cria_conexao():
    conn = sqlite3.connect('deploy.db')

    return conn
