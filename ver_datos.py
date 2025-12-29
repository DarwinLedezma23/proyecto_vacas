import sqlite3

conn = sqlite3.connect("vacas.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM vacas")
filas = cursor.fetchall()

for fila in filas:
    print(fila)

conn.close()