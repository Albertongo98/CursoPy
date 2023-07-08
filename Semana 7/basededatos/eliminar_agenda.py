# Se importa la librería para manipular base de datos
import sqlite3

"""Se abre conexión a la base de datos, 
en caso de no existir se crea el archivo de la base de datos"""
conexion = sqlite3.connect('agenda.db')

# Se crea un cursor
cursor = conexion.cursor()

# Se genera el texto de la consulta SQL de modificación de registro
sql = ''' DELETE FROM agenda WHERE id = ? '''

# Se ejecuta la consulta SQL para eliminar al contacto con el id = 1
cursor.execute(sql,(1,))
# Se confirma la modificación de los datos
conexion.commit()

# Validación cambio
cursor.execute("SELECT * FROM Agenda") # Se ejecuta la consulta de la tabla agenda
contactos = cursor.fetchall() # Se obtienen los datos de la consulta 
print(contactos)

# Se cierra conexión
conexion.close()