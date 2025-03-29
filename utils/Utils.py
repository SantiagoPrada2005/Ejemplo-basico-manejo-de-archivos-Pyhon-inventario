import os
import re
import UI as ui
import DataManager as dm
from utils.validar_input import validar_input

def validar_ruta(ruta : str) -> bool:
    """
    Valida que la ruta del archivo sea correcta usando expresiones regulares.
    Acepta rutas absolutas (Windows y Unix/Linux) y rutas relativas.
    Retorna True si la ruta es válida, False en caso contrario.
    """
    # Patrón para rutas relativas y absolutas
    patron = r'^(?:(?:[a-zA-Z]:\\|/)?|\.{1,2}/)?(?:[^<>:"/\\|?*\n\r]+/)*[^<>:"/\\|?*\n\r]*$'
    
    if not re.match(patron, ruta):
        return False
    
    try:
        # Convertir a ruta absoluta para verificar si el directorio padre existe
        ruta_absoluta = os.path.abspath(ruta)
        directorio_padre = os.path.dirname(ruta_absoluta)
        
        # Verificar si el directorio padre existe
        if not os.path.exists(directorio_padre):
            os.makedirs(directorio_padre, exist_ok=True)
        return True
    except (OSError, ValueError):
        return False

def validar_producto(productos):
    if productos is None:
        print("No hay productos en el inventario")
        return False
    return True

def buscar_producto(productos):
    if validar_producto(productos):
        ui.imprimir_titulo("Buscar producto")
        codigo = input("\nIngrese el código del producto: ")
        for producto in productos:
            if producto.codigo == codigo:
                ui.imprimir_producto(producto)
                return
        ui.imprimir_titulo("Producto no encontrado")
    else :
        ui.imprimir_titulo("No hay productos en el inventario")

def valor_inventario(productos):
    valor = 0
    if not validar_producto(productos):
        ui.imprimir_titulo("No hay productos en el inventario")
        return
    for producto in productos:
        valor += producto.precio * producto.cantidad
    ui.imprimir_titulo(f"El valor del inventario es: ${valor}")

def listar_productos(productos):
    if productos.__len__() == 0:
        os.system('clear')
        ui.imprimir_titulo("No hay productos en el inventario")
        return
    for producto in productos:
        ui.imprimir_producto(producto)

def cargar_archivo(archivos : list) -> list:
    total_archivos = len(archivos)
    for x, archivo in enumerate(archivos):
        print(f"{x+1}. {archivo}")
    try:
        opcion = int(validar_input(f"Seleccione una opción [0-{total_archivos}] -> ", r'[1-total_archivos]'))
        productos = dm.cargar_productos(ruta=str("docs/"+archivos[opcion-1]))
        return productos
    except Exception as e:
        print("Opción inválida")
    input("Presione enter para continuar...")

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')