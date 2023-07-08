from base_datos import BaseDatos
from autenticacion import Autenticacion
import sqlite3

class AdministracionInventario:
    
    baseDatos = None
    autenticacion = None
    # Definicion de nombre de base de datos y llamado de autenticacion
    def __init__(self):
        self.baseDatos = BaseDatos('inventario.db')
        self.autenticacion = Autenticacion()
        if self.baseDatos.verificarBaseDatosExiste():
            self.autenticacion.verificarAutenticacion()
        else:
            self.baseDatos.crearBaseDatos()
            self.baseDatos.crearTablaProductos()
# Muestra productos actuales en la base de datos inventario.db
    def mostrarListaProductos(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM productos")     
            productos = cursor.fetchall()
            if len(productos) > 0:
                print("Lista de productos disponibles: ")
                print("------------------------------------")
                for id,nombre_producto,descripcion,precio,stock in productos:
                    print('id: {}, nombre del producto: {}, descripción: {}, precio: {}, stock: {}'
                        .format(id, nombre_producto, descripcion, precio, stock))
                print("------------------------------------")
            else:
                print("No hay productos que mostrar")
                print("------------------------------------")
        except sqlite3.Error as e:
            print("Error al mostrar los datos de la tabla productos", e)
        finally:
            if conexion:
                cursor.close()
                conexion.close()
    #Agrega producto a la base de datos productos
    def agregarProducto(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            nombre_producto,descripcion,precio,stock = self.ingresarDatosProducto()
            valores = (nombre_producto, descripcion, precio, stock)
            sql = ''' INSERT INTO productos(nombre_producto,descripcion,precio,stock)
                    VALUES(?,?,?,?) '''
                    
            cursor.execute(sql,valores)
            conexion.commit()
            print("Datos guardados correctamente")
            print("------------------------------------")
        except sqlite3.Error as e:
            print('Error al intentar insertar los datos: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
    #Modifica el producto si existe si no nos indica que no esta dado de alta
    def modificarProducto(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            
            cursor.execute("SELECT * FROM productos")     
            productos = cursor.fetchall()
            if len(productos) > 0:
                
                print("Lista de productos para modificar:")
                self.mostrarListaProductos()
                print("----------------------------------")
                id_producto = self.ingresarID("Ingresa el id del producto a modificar \n")
                
                encontrar_producto = cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))    
                producto = encontrar_producto.fetchone()
                if producto :
                    nombre_producto,descripcion,precio,stock = self.ingresarDatosProducto()
                    sql = ''' UPDATE productos SET nombre_producto = ?, descripcion = ?, precio = ?, stock = ? WHERE id = ? '''
                    datos_producto = (nombre_producto,descripcion,precio,stock,id_producto)
                    cursor.execute(sql,datos_producto)
                    conexion.commit()
                    print("Registro modificado correctamente")
                    print("------------------------------------")
                else:
                    print("No hay registro con ese id")
                    print("------------------------------------")
            else:  
                print("No hay productos para modificar")
                print("------------------------------------")
            
        except sqlite3.Error as e:
            print('Error al intentar modificar el registro: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
    #Baja de productos
    def eliminarProducto(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM productos")     
            productos = cursor.fetchall()
            if len(productos) > 0:
            
                print("Lista de productos para eliminar:")
                self.mostrarListaProductos()
                print("------------------------------------")
                id_producto = self.ingresarID("Ingresa el id del producto a eliminar \n")
                
                encontrar_producto = cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))     
                if len(encontrar_producto.fetchall()) == 1:
                    sql = ''' DELETE FROM productos WHERE id = ? '''
                    cursor.execute(sql,(id_producto,))
                    conexion.commit()
                    print("Registro eliminado correctamente")
                    print("------------------------------------")
                else:
                    print("No hay registro con ese id")
                    print("------------------------------------")
            
            else:  
                print("No hay productos para eliminar")
                print("------------------------------------")
                
        except sqlite3.Error as e:
            print('Error al intentar eliminar el registro: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
    #Busca el ID y muestra si esta correctamente capturado
    def ingresarID(self,mensaje):
        id_producto = 0
        datos_incorrectos = True
        while datos_incorrectos:
            try:
                id_producto = int(input( mensaje ))
                datos_incorrectos = False
            except Exception as e:
                print('Error al capturar el id del producto: {}'.format(e))
                print('Intente de nuevo ingresar el id \n')
                datos_incorrectos = True
        return id_producto
    #Captura los datos del producto
    def ingresarDatosProducto(self):
        datos_incorrectos = True
        while datos_incorrectos:
            try:
                nombre_producto = input("Ingresa el nombre del producto \n")
                descripcion = input("Ingresa descripción del producto \n")
                precio = float(input("Ingresa el precio del producto \n"))
                stock = int(input("Ingresa el stock del producto \n"))
                datos_incorrectos = False
            except Exception as e:
                print('Error al capturar un dato: {}'.format(e))
                print('Intente de nuevo ingresar los datos \n')
                datos_incorrectos = True
        return nombre_producto,descripcion,precio,stock
    