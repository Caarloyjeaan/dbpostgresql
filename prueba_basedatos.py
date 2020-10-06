import psycopg2
from config import *

conexion = psycopg2.connect(user="postgres", password="Periferia2020", host="127.0.0.1", port="5432", database="postgres")

cursor = conexion.cursor()

cursor.execute('SELECT * FROM public.insertar_datos ORDER BY id')
registros = cursor.fetchall()

#Recupera todas las filas del resultado de una consulta (Tupla). 
print(registros)

cursor.close()
conexion.close()