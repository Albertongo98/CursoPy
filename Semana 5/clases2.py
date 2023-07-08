#Crear clases de perros

class perro:
    #Metodo init (inicializar valores) constructores
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    # Metodo ladrar
   
    def ladrar(self):
        print("guau!")

    #Metodo datos
    def datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Raza: {self.raza}")

#Fin de la definicion de la clase

nuevo_perro = perro("Boli", 2,"Chihuahua")

#Llamada al metodo ladrar

nuevo_perro.ladrar() #guau!

nuevo_perro.datos() #Nombre boli 2 años

can1 = perro ("Aludra", 2, "Callejero")

can1.ladrar()

can1.datos()
 