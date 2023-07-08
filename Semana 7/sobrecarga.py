#Ejemplo de sobrecarga con numero ilimitado de argumentos, parametros

class Calculadora:
    def sumar(self, *args):
        total = sum(args)
        return total
    
#Uso de la calculadora que suma 

calc = Calculadora()

#Suma dos numeros
resultadodosnumeros = calc.sumar(8,11)
print(resultadodosnumeros)

#Suma tres numeros
resultadotresnumeros = calc.sumar(5.2,9.7,10)
print (resultadotresnumeros)

#Suma de 5 numeros
resultado5numeros = calc.sumar(3,5,4,76,2)
print(resultado5numeros)

