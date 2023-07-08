#Alberto Madrid
#2 de mayo 2023
#Primer programa de calciulo de propinas
print("bienvenido a la calculadora de propinas")
#Entradas
cuenta = float (input("cual fue el monto de la comida?"))
porcentaje = int (input("que porcentaje desea otorgar 10, 20 30?"))
comensales = int (input("en cuantas personas se dividira la cuenta?"))
#Procesos
porcentaje_decimal = porcentaje / 100
propina = cuenta * porcentaje_decimal
total_cuenta = cuenta + propina
pago_x_persona = total_cuenta / comensales
pago_total = round(pago_x_persona,2) #funcion predefinida para redondear
#salida
print("cada persona pagará: $" , pago_total, "pesos")

