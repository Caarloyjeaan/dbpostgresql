import psycopg2
from config import *

conexion = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB)

cursor = conexion.cursor()
sentencia = 'DELETE FROM persona WHERE id_persona = %s' #%s es un comodin, que permite insertar valores dinánimcos
# valores = (9,)
entrada = input("Proporciona la pk a eliminar: ")
valores = (entrada, )
cursor.execute(sentencia, valores)
# Guardamos la información en la base de datos
conexion.commit()
registros_eliminados = cursor.rowcount
print(f'Registros eliminados: {registros_eliminados}')
cursor.close()
conexion.close()