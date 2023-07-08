# Función a realizarle una prueba
def sumar_dos_valores(valor_uno,valor_dos):
    return valor_uno + valor_dos

# Se declara la función que ejecutará la prueba
def testfuncion():
    # Se usa assert para comparar el valor devuelto
    assert sumar_dos_valores(5,5) == 10