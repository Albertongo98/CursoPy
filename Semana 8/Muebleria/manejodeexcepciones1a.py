#Manejo de excepciones (errores) con try - except
dividendo = 7
divisor = 4

try:
    resultado = dividendo/divisor
    print(resultado)
except ZeroDivisionError:
    print("Error: No es posible dividir entre cero")
    #Cualquier otra cosa que necesites