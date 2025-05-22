import sqlite3
import pandas as pd
import random
from faker import Faker
import os

fake = Faker()
conn = sqlite3.connect("personas.db")
cursor = conn.cursor()

def obtener_dias():
    return random.randint(1, 100)

# Crear 10 personas ficticias
lista_personas = [fake.uuid4() for _ in range(119390)]
viajes_data = []

for i in lista_personas:
    for j in range(6):
        id_persona = fake.ssn()
        nombre = fake.first_name()
        apellido = fake.last_name()
        email = fake.email()
        pais_origen = fake.country()
        ciudad_origen = fake.city()
        viajes_data.append((id_persona, nombre, apellido, email, pais_origen, ciudad_origen, obtener_dias()))

cursor.executemany("""
INSERT INTO personas (id_persona, nombre, apellido, mail, pais_origen, ciudad_destino, dias_viaje)
VALUES (?, ?, ?, ?, ?, ?, ?);
""", viajes_data)

conn.commit()
conn.close()
