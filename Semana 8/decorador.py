# Estructura básica de un decorador
def decorador(funcion):
    def funcion_decorada():
        print("Antes de ejecutar la función")
        funcion()
        print("Después de ejecutar la función")
    return funcion_decorada

@decorador
def mi_funcion():
    print("¡Hola, mundo!")

mi_funcion()