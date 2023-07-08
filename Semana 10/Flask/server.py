# Se importa el módulo de Flask
from flask import Flask

# Se declara la variable de la aplicación web
app = Flask(__name__)

# Se declara una ruta que corresponde al inicio del sitio
@app.route('/')
#Se declara la función que se asocia a la ruta
def primer_sitio():
    return 'Primer aplicación en Flask. Modificada'

# Decorador para asociar ruta a una función
@app.route('/hola')
# Función asociada a la ruta
def hola_mundo():
    # Valor a mostrar en el navegador
    return "hola mundo"

# Decorador para asociar ruta a una función con un parámetro
@app.route('/hola/<nombre>')
# Función obtiene el mismo parámetro que la ruta asociada
def hola_nombre(nombre):
    # Se usa el parámetro en la función
    return "Hola, " + str(nombre) + ", es un gusto saludarte."

# Decorador para asociar ruta a una función con más de un parámetro
@app.route('/sumar/<valor_uno>/<valor_dos>')
# Función obtiene los mismo parámetros que la ruta asociada
def sumar_numeros(valor_uno, valor_dos):
    # Se usa el parámetro en la función
    suma = int(valor_uno) + int(valor_dos)
    return 'La suma de los valores es ' + str(suma)