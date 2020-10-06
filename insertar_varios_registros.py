import psycopg2
from config import *

conexion = psycopg2.connect(user="postgres", password="Periferia2020", host="127.0.0.1", port="5432", database="postgres")

cursor = conexion.cursor()
# %s es un comodin, que permite insertar valores dinánimocs

#executemany para insertar varios registros
cursor.execute("INSERT INTO public.insertar_datos(nombre,apellido,email) VALUES ('Jose', 'Pepito', 'Sevilla'), ('Fernando', 'Francisco', 'Valencia'), ('Pedro', 'Agustín', 'Galicia')")

# Guardamos la información en la base de datos
conexion.commit()
registros_insertados = cursor.rowcount
print(f'Registros insertados: {registros_insertados}')
cursor.close()
conexion.close()
