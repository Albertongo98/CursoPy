import unittest


#Función de captura de texto

def capturar_texto():
    texto = input("Ingresa un texto: ")
    return texto


# Prueba unitaria para verificar que funcione correctamente la función de entrada de texto
class PruebaCapturarTexto(unittest.TestCase):
    def test_capturar_texto(self):
        texto = capturar_texto()
        self.assertEqual(texto, "¡Prueba exitosa!")

if __name__ == '__main__':
    unittest.main()