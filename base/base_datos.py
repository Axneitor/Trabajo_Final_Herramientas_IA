import sqlite3
import pandas as pd

conn = sqlite3.connect("personas2.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS personas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_persona INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    mail TEXT NOT NULL,
    pais_origen TEXT NOT NULL,
    ciudad_destino TEXT NOT NULL,
    dias_viaje INTEGER NOT NULL
);
""")

conn.commit()
conn.close()
