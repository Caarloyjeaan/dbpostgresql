import psycopg2
from config import *

conexion = psycopg2.connect(user="postgres", password="Periferia2020", host="127.0.0.1", port="5432", database="postgres")

cursor = conexion.cursor()
# %s es un comodin, que permite insertar valores dinánimcos
sentencia = 'UPDATE public.insertar_datos SET nombre = %s, apellido = %s, email = %s WHERE id = %s'
valores = (('Juan', 'Perez', 'jperez@mail.com', 2),
           ('Emma1', 'Gomez', 'egomez1@mail.com', 10),
           )
cursor.executemany(sentencia, valores)
# Guardamos la información en la base de datos
conexion.commit()
registros_actualizados = cursor.rowcount
print(f'Registros actualizados :{registros_actualizados}')
cursor.close()
conexion.close()
