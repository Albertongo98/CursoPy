# Creación de agenda para contactos

import sqlite3

# Se crea la conexión a la base de datos, en caso de no existir, es creada
conexion = sqlite3.connect("agenda.db")

# Creación de la tabla de la agenda
conexion.execute('''CREATE TABLE agenda (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                 Nombre TEXT NOT NULL, 
                 Direccion TEXT NOT NULL,
                 Telefono CHAR(10)
                 );''')

# Cerrar conexión
conexion.close()
print("Ejecución correcta")