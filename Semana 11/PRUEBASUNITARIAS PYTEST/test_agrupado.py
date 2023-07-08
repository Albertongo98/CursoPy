#Se importa el modulo pytest
import pytest 

# Se importa las funciones o bloques a realizarle pruebas
from funciones_probar import *

# Se declara la clase de las pruebas
class TestAgrupacionClase:
    # Se define la primera función con las reglas de convención de Pytest
    def test_uno(self):
        valor = "Alberto"
        assert invertir_cadena(valor) == "otreblA"

# Se define la segunda función con las reglas de convención de Pytest
    # Se agrega el decorador para mandar parámetros a la prueba
    @pytest.mark.parametrize("entrada, salida",[(1,1),(2,2),(3,6),(4,24)])
    def test_dos(self, entrada,salida):
        assert obtener_factorial(entrada) == salida