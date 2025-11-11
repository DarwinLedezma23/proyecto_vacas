import sqlite3 

def crear_tabla():
    conn = sqlite3.connect("vacas.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vacas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        fecha_inseminacion TEXT,
        cantidad_partos INTEGER,
        fecha_posible_parto TEXT,
        fecha_secado TEXT,
        concepcion exitosa TEXT,
        observaciones TEXT
    )
    """)
    conn.commit()
    conn.close()

def insertar_vaca(nombre, fecha_inseminacion, cantidad_partos, fecha_posible_parto, fecha_secado, concepcion_exitosa, observaciones):
        conn = sqlite3.connect("vacas.db")
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO vacas (nombre, fecha_inseminacion, cantidad_partos, fecha_posible_parto, fecha_secado, concepcion_exitosa, observaciones)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (nombre, fecha_inseminacion, cantidad_partos, fecha_posible_parto, fecha_secado, concepcion_exitosa, observaciones))
        conn.commit()
        conn.close()
        