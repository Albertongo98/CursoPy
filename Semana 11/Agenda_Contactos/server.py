import json
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    encabezado_pagina = "Listado de contactos"
    titulo_pagina = "Lista de contactos"
    contactos = obtenerJSON("contactos.json")
    return render_template("lista_contactos.html", 
                        encabezado_pagina = encabezado_pagina, 
                        titulo_pagina = titulo_pagina,
                        contactos = contactos)
    
@app.route('/datos/contacto/<id>')
def datos_contacto(id):
    encabezado_pagina = "Datos de contacto"
    contactos = obtenerJSON("contactos.json")
    contacto_encontrado = None
    titulo_pagina = None
    for contacto in contactos:
        if contacto['id'] == int(id):
            contacto_encontrado = contacto
            titulo_pagina = "Datos de " + contacto_encontrado['name']
            break
    
    return render_template("datos_contacto.html", 
                        encabezado_pagina = encabezado_pagina, 
                        titulo_pagina = titulo_pagina,
                        contacto_encontrado = contacto_encontrado)
def obtenerJSON(nombre_archivo ):
    datos = {}
    try:
        with open(nombre_archivo) as archivo:
            datos = json.load(archivo)
    except Exception as e:
        print('Error al leer el archivo: {}'.format(e))
    return datos
    
    