import psycopg2
from config import *

conexion = psycopg2.connect(user="postgres", password="Periferia2020", host="127.0.0.1", port="5432", database="postgres")

cursor = conexion.cursor()
sentencia = 'SELECT * FROM public.insertar_datos WHERE id IN %s' # IN permite seleccionar varios valores
entrada = input("Proporciona las pk a buscar (separado por comas): ")
tupla = tuple(entrada.split(','))
print(tupla)
llaves_primarias = (tupla,)
# id_persona = input("Proporciona la llave primaria a buscar: ")
# Parametros que pasemos a la sentencia deben ser una tupla
cursor.execute(sentencia, llaves_primarias)
registros = cursor.fetchall()
for registro in registros:
    print(registro)

cursor.close()
conexion.close()