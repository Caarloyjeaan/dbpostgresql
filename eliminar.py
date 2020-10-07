import psycopg2
from config import *

conexion = psycopg2.connect(user="postgres", password="Periferia2020", host="127.0.0.1", port="5432", database="postgres")

cursor = conexion.cursor()
sentencia = 'DELETE FROM public.insertar_datos WHERE id = %s' #%s es un comodin, que permite insertar valores dinánimcos
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