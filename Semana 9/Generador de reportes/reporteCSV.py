import json
import csv

class lectorJSON:
    
    def obtenerJSON(self, nombre_archivo ):
        datos = {}
        try:
            with open(nombre_archivo) as archivo:
                datos = json.load(archivo)
        except Exception as e:
            print('Error al leer el archivo: {}'.format(e))
        return datos

    def simplificarJSON(self, datos):
        dict_temporal = []
        for item in datos:
            for key,value in item.items():
                if type(value) is list:
                    temp = item.copy()
                    del temp[key]
                    dict_temporal.append(temp)
        return dict_temporal
    
    def crearCSV(self, archivo_salida, datos, encabezados):
         with open(archivo_salida, 'w') as archivo:
            writer = csv.DictWriter(archivo, fieldnames = list(encabezados))
            writer.writeheader()
            writer.writerows(datos)
            
    def convertirJSONaCSV(self,nombre_archivo,coleccion,archivo_salida):
        headers = []
        datos = self.obtenerJSON(nombre_archivo)
        if (len(datos) > 0):
            if coleccion not in datos:
                print("La colección solicitada no existe")
            else:
                datos_reporte = self.simplificarJSON(datos[coleccion])
                self.crearCSV(archivo_salida, datos_reporte, datos_reporte[0])
        else:
            print("No hay datos para generar CSV")
