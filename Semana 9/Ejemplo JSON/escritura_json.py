import json

try:
    # Intenta leer el archivo JSON existente
    with open('nuevojson.json') as archivo:
        datos = json.load(archivo)
        print(datos)
except FileNotFoundError:
    # Si el archivo no existe, crea un nuevo diccionario vacío
    datos = {}

# Escribir en un archivo JSON
datos = {
    "nombre": "Fernando",
    "edad": 18,
    "ciudad": "Chihuahua",
    "intereses": ["programación", "viajes", "música"],
    "activo": True,
    "trabajo": None
}

with open('nuevojson.json', 'w') as archivo:
    json.dump(datos, archivo)