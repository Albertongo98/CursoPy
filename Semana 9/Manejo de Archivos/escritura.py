#Crear contenido en un archivo nuevo

archivo = open("nuevo_archivo.txt", "w")
contenido = "este contenido es nuevo para un archivo"
archivo.write(contenido)
print(contenido)
archivo.close
