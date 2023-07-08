#9 de mayo 2023
#Alberto Madrid
#Definicion de funciones

def  saludar ():
    print ("Hola programador")
    suma = 5+8 
    print (suma)
    pass

saludar()
####################################################################

def saludar2(nombre):
    print ("¡Hola",nombre,"!")
    
#Llamar a la persona
saludar2("Alberto")

####################################################################

def doble(num):
    return num * 2

#Llamo a la funcion y guardar resultado en una variable
resultado = doble(18)

#imprime el numero al doble
print ("El doble de tu numero es:",resultado)

####################################################################

#Formula para calcular el area de un triangulo
base = float(input("dame el valor de la base: "))
altura = float(input("dame el valor de la altura: "))

def AreaTriangulo(base,altura):
    area = (base * altura)/2
    return area

#Llamar funcion
AreaFinal = AreaTriangulo(base,altura)
print("El area final de triangulo es: ", AreaFinal)

####################################################################

#Funcion de tipo lamda
suma =lambda x,y: x + y

print(suma (3,5))
