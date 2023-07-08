# Se importa la librería para manipular base de datos
import sqlite3

"""Se abre conexión a la base de datos, 
en caso de no existir se crea el archivo de la base de datos"""
conexion = sqlite3.connect('agenda.db')

cursor = conexion.cursor()

valores = [('Contacto 1', 'Dirección 1', '9900000000'),
           ('Contacto 2', 'Dirección 2', '9900000000'),
           ('Contacto 3', 'Dirección 3', '9900000000')]
sql = ''' INSERT INTO Agenda(nombre,direccion,telefono)
        VALUES(?,?,?) '''
        
cursor.executemany(sql,valores)

conexion.commit()
# Se cierra conexión
conexion.close()