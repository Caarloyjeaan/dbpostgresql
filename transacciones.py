import psycopg2
from config import *

conexion = psycopg2.connect(user="postgres", password="Periferia2020", host="127.0.0.1", port="5432", database="postgres")

# conexion.autocommit = True # Solo para pruebas por lo general
#El trybloque le permite probar un bloque de código en busca de errores.
try:
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO public.insertar_datos(nombre, apellido, email) VALUES(%s, %s, %s)' #%s es un comodin, que permite insertar valores dinánimocs
    valores = ('Ethan', 'Daniel', 'danielespitia1@outlook.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE public.insertar_datos SET nombre = %s, apellido = %s, email = %s WHERE id = %s' #%s es un comodin, que permite insertar valores dinánimcos
    valores = ('Juan1', 'Perezoso2', 'jperez2@mail.com', 18)
    cursor.execute(sentencia, valores)

    # Guardamos la información en la base de datos
    conexion.commit()
#El exceptbloque le permite manejar el error.
except Exception as e:
    # Rollback da marcha atras a todas las operaciones SQL pendientes
    conexion.rollback()
    print(f"Ocurrió un error en la transacción: {e}")
#El finallybloque le permite ejecutar código, independientemente del resultado de los bloques try y except.
finally:
    cursor.close()
    conexion.close()