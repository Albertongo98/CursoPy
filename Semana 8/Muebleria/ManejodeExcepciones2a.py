#Manejo de excepciones en escritura/lectura de archivos de texto
try:
    archivo = open ("archivo.txt", "r")
    contenido = archivo.read()
    
#Posibles excepciones de escritura/lectura para un archivo externo
except FileNotFoundError:
    archivo = open("archivo.txt", "w")
    print("Archivo no se encontro pero fue creado")
except PermissionError:
    print("No tienes acceso al archivo")
except IOError:
    print ("Error de entrada y/o salida al leer/escribir el archivo")
else:
    print("Aqui esta el contenido del archivo")
    print(contenido)
    archivo.close
    print("El archivo ah sido cerrado correctamente")
    