import psycopg2
from config import *

conexion = psycopg2.connect(user="postgres", password="Periferia2020", host="127.0.0.1", port="5432", database="postgres")

cursor = conexion.cursor()
# %s es un comodin, que permite insertar valores dinánimocs
sentencia = 'INSERT INTO public.insertar_datos(nombre, apellido, email) VALUES(%s, %s, %s)'
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
