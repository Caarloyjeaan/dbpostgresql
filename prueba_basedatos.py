import psycopg2
from config import *

conexion = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB)

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona ORDER BY id_persona'
cursor.execute(sentencia)
registros = cursor.fetchall()
print(registros)

cursor.close()
conexion.close()