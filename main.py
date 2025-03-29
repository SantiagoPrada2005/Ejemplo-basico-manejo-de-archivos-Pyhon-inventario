import Producto
import DataManager as dm
import os
import UI as ui
from utils.Utils import buscar_producto, valor_inventario, listar_productos, cargar_archivo, limpiar_consola
from utils.validar_input import validar_input


productos = []

def menu():
    global productos
    productos = dm.cargar_productos()
    opcion = None
    while opcion != 0:
        limpiar_consola()
        ui.imprimir_menu()

        opcion = int(validar_input("Seleccione una opción [0-6] -> ", r'[0-6]'))

        #Opciones del menú
        if opcion == 1:
            #Agregar producto al inventario
            limpiar_consola()
            dm.agregar_producto(productos,Producto.Producto(None, None, None, None))
        elif opcion == 2:
            #Buscar producto en el inventario por codigo
            limpiar_consola()
            buscar_producto(productos);input("Presione enter para continuar...")
        elif opcion == 3:
            limpiar_consola()
            listar_productos(productos);input("Presione enter para continuar...")
        elif opcion == 4:
            limpiar_consola()
            valor_inventario(productos);input("Presione enter para continuar...")
        elif opcion == 5:
            limpiar_consola()
            dm.exportar_productos(productos);input("Presione enter para continuar...")
        elif opcion == 6:
            limpiar_consola();print("")
            archivos = os.listdir("docs")
            productos = cargar_archivo(archivos)
        elif opcion == 0:
            print("Saliendo del sistema...")
        else:
            print("Opción inválida");input("Presione enter para continuar...")
    print("Gracias por usar el sistema de inventario\nGuardando productos...")
    dm.exportar_productos(productos,'docs/productos.dat')

if __name__ == "__main__":
    menu()