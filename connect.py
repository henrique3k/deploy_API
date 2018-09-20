import sqlite3

conn = sqlite3.connect('deploy.db')

cursor = conn.cursor()



conn.close()