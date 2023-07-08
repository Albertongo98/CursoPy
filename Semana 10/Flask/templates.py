# Se importa el módulo render_template
from flask import Flask, render_template

# Se declara la variable de la aplicación web y se específica la carpeta de los templates
app = Flask(__name__, template_folder="templates")

# Se declara una ruta que corresponde al inicio del sitio
@app.route('/')
#Se declara la función que se asocia a la ruta
def primer_sitio():
	# Se implementan la función para renderizar el template html
    return render_template("index.html")

# Ruta con template y variables en template
@app.route('/articulos')
def listar_productos():
    encabezado_pagina = "Listado de artículos"
    titulo_pagina = "Lista de artículos"
    #Se declara una lista
    articulos = [
        'Mesa de centro',
        'Silla de madera',
        'Sofá reclinable'
    ]
    # Se pasan variables a través de la función render_template
    return render_template("productos.html", 
                        encabezado_pagina = encabezado_pagina, 
                        titulo_pagina = titulo_pagina,
                        articulos = articulos
            )