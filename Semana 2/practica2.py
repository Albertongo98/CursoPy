#AlbertoMadrid
#2 de mayo 2023
# Calculadora de masa corporal

#entradas
peso = float (input("ingresa tu peso: "))
estatura = float (input(" ingresa tu estatura en metros: "))

#proceso
imc = round ((peso/estatura**2),2)
print ("tu IMC es: ",imc)

#estructura condicional
if imc >= 30:
    print("obesidad")
elif imc >= 25:
    print ("sobrepeso")
elif imc > 18.5:
    print("normal")
else:
    print("peso bajo")
    
