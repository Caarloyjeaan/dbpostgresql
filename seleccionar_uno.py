import psycopg2
from config import *

conexion = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB)

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
# id_persona = 2
id_persona = input("Proporciona la llave primaria a buscar: ")
llave_primaria = (id_persona,) # al final ',' para que se cree de tipo tupla
# Parametros que pasemos a la sentencia deben ser una tupla
cursor.execute(sentencia, llave_primaria)
registros = cursor.fetchone()
print(registros)

cursor.close()
conexion.close()