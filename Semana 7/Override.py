# Anulacion de metodo (method overrriding)

class Empleado():
    def CalcularSueldo(self,DiasPagados,PagoPorDia):
        return DiasPagados * PagoPorDia
    
class EmpleadoTemporal(Empleado):
    def CalcularSueldo(self, DiasPagados, PagoPorDia, Bono):
        return DiasPagados * PagoPorDia + Bono

base = Empleado()
ventas = EmpleadoTemporal()

dias = int(input("Cuantos dias son del periodo?"))
sueldodia = float(input("Cual es el pago por dia?"))
bono = float(input("Define el bono"))
print ("El pago al empleado base es {}".format(base.CalcularSueldo(dias,sueldodia)))
print ("El pago al empleado de ventas es {}".format(ventas.CalcularSueldo(15,250,2000)))
