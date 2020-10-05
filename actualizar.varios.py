import psycopg2
from config import *

conexion = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB)

cursor = conexion.cursor()
# %s es un comodin, que permite insertar valores dinánimcos
sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
valores = (('Juan', 'Perez', 'jperez@mail.com', 1),
           ('Emma1', 'Gomez', 'egomez1@mail.com', 2),
           )
cursor.executemany(sentencia, valores)
# Guardamos la información en la base de datos
conexion.commit()
registros_actualizados = cursor.rowcount
print(f'Registros actualizados :{registros_actualizados}')
cursor.close()
conexion.close()
