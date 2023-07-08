#Manejo de excepciones en escritura/lectura de archivos de texto
try:
    archivo = open ("archivo.txt", "r")
    
#Posibles excepciones de escritura/lectura para un archivo externo
except FileNotFoundError:
    print("Archivo no se encuentra")
except PermissionError:
    print("No tienes acceso al archivo")
except IOError:
    print ("Error de entrada y/o salida al leer/escribir el archivo")
else:
    print("Pudiste abrir el archivo")
    