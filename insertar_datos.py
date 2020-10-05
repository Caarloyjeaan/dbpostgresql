import psycopg2
from config import *

conexion = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB)

cursor = conexion.cursor()
sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)' #%s es un comodin, que permite insertar valores dinánimocs
valores = ('Carlos', 'Lara', 'clara@mail.com')
cursor.execute(sentencia, valores)
# Guardamos la información en la base de datos
conexion.commit()
registros_insertados = cursor.rowcount
print(f'Registros insertados :{registros_insertados}')
cursor.close()
conexion.close()