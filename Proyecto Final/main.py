#Proyecto final Happy Burguer

#Importacion de modulos
from mispaquetes import CC

def MenuPrincipal():
    opcion = ""
    
    while opcion != "s":
        print("Bienvenidos a Happy Burguer!")
        print("a. Pedidos")
        print("b. Clientes")
        print("c. Menu")
        print("s. Salir")
        
        opcion = input("\n Selecciona una opcion: \n")
        
        if opcion == "a":
            #print("Elegiste Pedidos")
            #Se ejecuta el pedido
            CapturaProductos()
        elif opcion == "b":
            print("Elegiste Clientes")
            CC.cliente()
        elif opcion == "c":
            print("Elegiste Menu")
        elif opcion == "s":
            print("Elegiste Salir")
        else:
            print("La opcion es Invalida")
            
#Pide datos de los productos y los muestra
def CapturaProductos():
    nombre = input("Ingresa el nombre del producto: ")
    precio = float(input("Ingresa el precio del producto: "))  
    unidades = int(input("Ingresa el numero de unidades a pedir: "))
    
    #Se calcula el total del pedido
    #TotalPedido = precio * unidades
    
    print("\n Datos del pedido \n")
    print("Tu producto es: ", nombre)
    print("El precio unitario es: ", precio)
    print("El total de unidase es: ", unidades)
    print("El total del pedido es: ",CalculoTotalPedido(precio,unidades))

def CalculoTotalPedido(uno,dos):
    return uno * dos

#Inicia la ejecucion del menu
MenuPrincipal()

    