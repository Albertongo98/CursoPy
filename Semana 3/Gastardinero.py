#Albertongo98
#9 mayo 2023

print("dinero a gastar: ")
dinero = float(input())

while dinero >0:
    print("¿Cuanto cuesta tu articulo?: ")
    costo = float(input())
    if dinero >= costo :
        dinero = dinero-costo
        print ("Lo pudiste comprar, te queda", dinero)
    elif (costo>dinero):
        print("no lo pudiste comprar, intenta de nuevo")
        
    if dinero ==0:
        print ("No hay dinero")
        break