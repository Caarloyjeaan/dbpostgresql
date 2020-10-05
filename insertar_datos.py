import psycopg2
from config import *

#Conexion con las base de datos
conexion = psycopg2.connect(user="postgres", password="Periferia2020", host="127.0.0.1", port="5432", database="postgres")



cursor = conexion.cursor()
#cursor.execute = 'INSERT INTO public.insertar_datos(nombre, apellido, email) VALUES(%s, %s, %s)' #%s es un comodin, que permite insertar valores dinánimocs
#valores = ('Carlos', 'Lara', 'clara@mail.com')
cursor.execute("INSERT INTO public.insertar_datos VALUES ('Hector', 'Castaño', 'hector@ejemplo.com')")

# Guardamos la información en la base de datos
conexion.commit()
registros_insertados = cursor.rowcount
print(f'Registros insertados :{registros_insertados}')
cursor.close()
#cierra la conexion 
conexion.close()