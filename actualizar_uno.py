import psycopg2
from config import *

conexion = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB)

cursor = conexion.cursor()
sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s' #%s es un comodin, que permite insertar valores dinánimcos
valores = ('Juan', 'Perezoso', 'jperez3@mail.com', 1)
cursor.execute(sentencia, valores)
# Guardamos la información en la base de datos
conexion.commit()
registros_actualizados = cursor.rowcount
print(f'Registros actualizados :{registros_actualizados}')
cursor.close()
conexion.close()