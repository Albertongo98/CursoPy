def invertir_cadena(cadena):
        return cadena[::-1]
    
def obtener_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
        print(i)
    return factorial