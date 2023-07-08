# Conversión de tipos de datos

class Convertidor():
    def ConvertirValor(self,valor):
        if type(valor) == int:
            return str(valor)
        elif type(valor) == str:
            return int(valor)
        
miobjeto = Convertidor()

valorPrimero = miobjeto.ConvertirValor(18)
valorSegundo = miobjeto.ConvertirValor("18")

print("El valor del primero objeto es {}".format(type(valorPrimero)))
print("El valor del segundo objeto es {}".format(type(valorSegundo)))