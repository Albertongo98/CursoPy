#Eliminar archivo .txt

import os

if os.path.exists("archivo.txt"):
    os.remove("archivo.txt")
    print("El archivo ah sido eliminado")
else:
    print("El archivo no existe")