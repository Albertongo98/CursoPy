# Se crea un cursor
cursor = conexion.cursor()

# Se genera el texto de la consulta SQL de modificación de registro
sql = ''' DROP TABLE agenda '''

# Se ejecuta la consulta SQL para eliminar al contacto con el id = 1
cursor.execute(sql)
# Se confirma la modificación de los datos
conexion.commit()

# Validación eliminación
print("Tabla eliminada")

# Se cierra conexión
conexion.close()