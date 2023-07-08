#Genera grafico con dos ejes

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,8,6,4,2]
plt.plot(x,y)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Grafico de linea')
plt.show()