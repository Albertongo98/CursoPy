# Se importa la librería para manipular base de datos
import sqlite3

"""Se abre conexión a la base de datos, 
en caso de no existir se crea el archivo de la base de datos"""
conexion = sqlite3.connect('agenda.db')

# Se crea un cursor
cursor = conexion.cursor()

# Se ejecuta la consulta de la tabla agenda
cursor.execute("SELECT * FROM Agenda")

# Se obtienen los datos de la consulta       
contactos = cursor.fetchall()

# Se iteran los datos devueltos en la consulta y se imprimen uno a uno
for contacto in contactos:
    print(contacto)

# Se cierra conexión
conexion.close()