# Clase Clientes para alta, modificación y borrado de clientes.
def cliente():

    class Cliente:
        def __init__(self, nombre, direccion, correo_electronico, telefono):
            self.nombre = nombre
            self.direccion = direccion
            self.correo_electronico = correo_electronico
            self.telefono = telefono

        def mostrar_cliente(self):
            print("Nombre:", self.nombre)
            print("Dirección:", self.direccion)
            print("Correo electrónico:", self.correo_electronico)
            print("Teléfono:", self.telefono)


    # Diccionario para almacenar los clientes
    clientes = {}

    # Función para mostrar el menú y obtener la opción del usuario
    def mostrar_menu():
        print("\n--- Menú Clientes---")
        print("1. Agregar cliente")
        print("2. Mostrar clientes")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Salir")
        return input("Ingrese el número de opción deseada: ")


    # Función para agregar un nuevo cliente
    def agregar_cliente():
        clave = input("Ingrese la clave del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")
        direccion = input("Ingrese la dirección del cliente: ")
        correo = input("Ingrese el correo electrónico del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        cliente = Cliente(nombre, direccion, correo, telefono)
        clientes[clave] = cliente
        print("Cliente agregado correctamente.")

    # Función para mostrar todos los clientes
    def mostrar_clientes():
        if clientes:
            print("\n--- Lista de Clientes ---")
            for clave, cliente in clientes.items():
                print("Clave:", clave)
                cliente.mostrar_cliente()
                print("------------------------")
        else:
            print("No hay clientes registrados.")

    # Función para modificar un cliente
    def modificar_cliente():
        clave = input("Ingrese la clave del cliente que desea modificar: ")
        cliente = clientes.get(clave)
        if cliente:
            cliente.mostrar_cliente()
            print("Ingrese los nuevos datos del cliente:")
            nombre = input("Nuevo nombre: ")
            direccion = input("Nueva dirección: ")
            correo = input("Nuevo correo electrónico: ")
            telefono = input("Nuevo teléfono: ")
            cliente.nombre = nombre
            cliente.direccion = direccion
            cliente.correo_electronico = correo
            cliente.telefono = telefono
            print("Cliente modificado correctamente.")
        else:
            print("Cliente no encontrado.")

    # Función para eliminar un cliente
    def eliminar_cliente():
        clave = input("Ingrese la clave del cliente que desea eliminar: ")
        cliente = clientes.get(clave)
        if cliente:
            cliente.mostrar_cliente()
            confirmacion = input("¿Está seguro/a de eliminar este cliente? (s/n): ")
            if confirmacion.lower() == "s":
                del clientes[clave]
                print("Cliente eliminado correctamente.")
            else:
                print("Eliminación de cliente cancelada.")
        else:
            print("Cliente no encontrado.")

    # Programa principal
    opcion = ""
    while opcion != "5":
        opcion = mostrar_menu()

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            modificar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            print("De regreso al menú principal")
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")