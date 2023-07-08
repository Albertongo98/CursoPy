#Alberto Madrid
#9 mayo 2023

#libreria para obtener valores aleatorios
import random

#listas base para generar contraseñas
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] 

#Pedirle al usuario cuantos de cada elemento contendra su contraseña

tot_letras = int(input("numero de letras: "))
tot_numeros = int(input("Cantidad de numeros: "))
tot_simbolos = int(input("Numero de simbolos: "))

#Generar la contraseña

password = []

for i in range(tot_letras):
    password.append(random.choice(letras))
for i in range(tot_numeros):
    password.append(random.choice(numeros))
for i in range(tot_simbolos):
    password.append(random.choice(simbolos))
    
#Mezclar elementos de la lista
random.shuffle(password)
        
#Convertir lista a texto, funcion join
nuevo_password = "".join(password)

#imprimir el nuevo password
print(f"Tu nueva contraseña es: {nuevo_password}")



