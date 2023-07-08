#Alberto Madrid
#2 mayo 2023
#ejercicio de estructuras de datos en python

#crear una lista
lista = ["lunes" , "martes" , "miercoles"]
print (lista)
lista.append("jueves")
lista.extend(["viernes", "sabado"])
lista.remove("martes")
lista.pop(3)
lista.append("lunes")
numeros = [1,2,3,4,5]
numeros.remove(2)
numeros.pop(0)
print(numeros)
#crear una tupla
deportes = ("beisbol", "futbol", "Basquetbol")
type(deportes)
len(deportes)
#inmutable pero mas rapido y seguro
#crear un diccionario
#tinen 2 elementos, llave y valor
dicnumeros = { 1:"texto", 2:25.36, 3:True,4:12}
type(dicnumeros)





#crear un conjunto(sets)
conjunto = {2,4,8,3}
type(conjunto)
conjunto.add(7)
conjunto.add(7)
conjunto2 = {"lunes", "martes","miercoles"}
type(conjunto2)
conjunto2.add("texto")
conjunto2
conjCong=frozenset ([5, "texto", 6.8])
conjCong.add("prueba") #no agrega
type(conjCong)
