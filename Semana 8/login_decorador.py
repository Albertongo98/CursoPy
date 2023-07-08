# Se deine el metodo que sera el decorador

def verifcar_login(funcion):
    user= "admin"
    password = "123"
    
    #Se declara una funcion retornada por el decorador
    def nueva_funcion():
        if user == "admin" and password =="123":
            funcion() #Esta func es la que nos dice si pudimos ingresar
        else:
            print("Usuario o contraseña incorrectos")
    return nueva_funcion
    
@verifcar_login
def mostrar_mensaje():
    print("Login exitoso")
    
#Programa principal, llamado al metodo decorado
mostrar_mensaje()
