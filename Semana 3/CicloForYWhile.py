#Alberto Madrid
#9 mayo 2023

for x in range(1,6):
    print("Este es el numero: %d" % (x))

    
for x in range(1,11):
    for y in range (1,11):
        print('%d * %d = %d' % (x,y,x*y))
        
####################################################################

superheroes =["ironman","batman","spiderman", "chapulin colorado"]

#mostrar heroes

for w in superheroes:
    print(f"yo soy {w}")
    
####################################################################

print("Ingresa tu edad \n")
edad = int(input())

for x in range(1,edad):
    print("Años vividos anteriormente: %d" % (x))
    
print("Tu vida ah sido buena")

####################################################################

captura = ''

while captura.lower() != 'fin':
    captura = input("escribe algo o escribe fin para terminar: ")
    
#while que cuenta hasta el numero 5

i = 1
while i < 6:
    print("este es el numero", i)
    if i == 3:
        break
    i += 1
print("while finalizado")
