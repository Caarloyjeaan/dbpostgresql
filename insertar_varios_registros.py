import psycopg2
from config import *

conexion = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB)

cursor = conexion.cursor()
# %s es un comodin, que permite insertar valores dinánimocs
sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
valores = (('Marcos', 'Cantu', 'mcantu@mail.com'),
           ('Angel', 'Quintana', 'aquintana@mail.com'),
           ('Maria', 'Gonzales', 'mgonzales@mail.com'))
cursor.executemany(sentencia, valores) #executemany para insertar varios registros
# Guardamos la información en la base de datos
conexion.commit()
registros_insertados = cursor.rowcount
print(f'Registros insertados: {registros_insertados}')
cursor.close()
conexion.close()
