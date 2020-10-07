import psycopg2
from config import *

conexion = psycopg2.connect(user="postgres", password="Periferia2020", host="127.0.0.1", port="5432", database="postgres")

cursor = conexion.cursor()
sentencia = 'SELECT * FROM public.insertar_datos WHERE id = %s'
# id_persona = 2
id_persona = input("Proporciona la llave primaria a buscar: ")
llave_primaria = (id_persona,) # al final ',' para que se cree de tipo tupla
# Parametros que pasemos a la sentencia deben ser una tupla
cursor.execute(sentencia, llave_primaria)
registros = cursor.fetchone()
print(registros)

cursor.close()
conexion.close()