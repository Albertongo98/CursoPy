from reporteCSV import lectorJSON

nombre_archivo = "posts.json"
coleccion = 'posts'
archivo_salida = 'reporte.csv'
reporteador = lectorJSON()
reporteador.convertirJSONaCSV(nombre_archivo,coleccion,archivo_salida)