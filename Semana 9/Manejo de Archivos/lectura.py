#Lectura de archivo de texto

archivo = open("archivo.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()
