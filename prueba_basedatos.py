import psycopg2
from config import *

conexion = psycopg2.connect(user="postgres", password="Periferia2020", host="127.0.0.1", port="5432", database="postgres")

cursor = conexion.cursor()
sentencia = 'SELECT * FROM public.insertar_datos ORDER BY id'
cursor.execute(sentencia)

#Recupera todas las filas del resultado de una consulta (Tupla). 
registros = cursor.fetchall()
print(registros)

cursor.close()
conexion.close()