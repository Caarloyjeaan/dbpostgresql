import psycopg2
from config import *

conexion = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB)

# conexion.autocommit = True # Solo para pruebas por lo general
try:
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)' #%s es un comodin, que permite insertar valores dinánimocs
    valores = ('Mario', 'Gomez', 'mgomez@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s' #%s es un comodin, que permite insertar valores dinánimcos
    valores = ('Juan1', 'Perezoso2', 'jperez2@mail.com', 1)
    cursor.execute(sentencia, valores)

    # Guardamos la información en la base de datos
    conexion.commit()
except Exception as e:
    # Rollback da marcha atras a todas las operaciones SQL pendientes
    conexion.rollback()
    print(f"Ocurrió un error en la transacción: {e}")

finally:
    cursor.close()
    conexion.close()