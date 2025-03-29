import pickle
from utils.Utils import validar_ruta
from Producto import Producto

def manipular_archivo(ruta = 'docs/productos.dat', productos=None, mode = 'rb'):
    """
    Carga los productos almacenados desde el archivo 'docs/productos.dat'.
    Modos del manejo del archivo:
        wb: Escritura binaria
        rb: Lectura binaria
        ab: Escritura binaria al final del archivo
        wb+: Lectura y escritura binaria
        rb+: Lectura y escritura binaria
        ab+: Lectura y escritura binaria al final del archivo
    """
    if not validar_ruta(ruta):
        print("Ruta inválida")
        return

    try:
        if productos is not None:
            with open(ruta, 'wb') as archivo:
                pickle.dump(productos, archivo)
                return
        else:
            with open(ruta, mode) as archivo:
                productos = pickle.load(archivo)
                return productos 
    except FileNotFoundError:
        print("No se encontró el archivo de productos")
        opcion = input("Desea crear un nuevo archivo de productos? (s/n) -> ")
        if opcion.lower() == 's':
            with open(ruta, 'wb') as archivo:
                productos = []
                pickle.dump(productos, archivo)
                print("Archivo no encontrado, fue creado uno nuevo")
        else:
            print("No se encontró el archivo de productos")
    except Exception as e:
        print(f"Ocurrió un error al cargar los productos: {e}")
    print("Productos cargados correctamente")
    return productos

def cargar_productos(ruta = 'docs/productos.dat'):
    """
    Carga los productos almacenados desde el archivo 'docs/productos.dat'.
    
    Lee una lista serializada de productos desde un archivo binario usando pickle.
    
    Returns:
        list: Lista de objetos Producto cargados desde el archivo.
        
    Raises:
        FileNotFoundError: Si el archivo 'docs/productos.dat' no existe.
        Exception: Si hay un error al cargar los productos.
    """

    productos = manipular_archivo(ruta=ruta)
    return productos

def exportar_productos(productos : list , ruta : str = 'docs/export.dat'):
    """
    Guarda la lista de productos en el archivo 'docs/productos.dat'.
    
    Lee los productos existentes y los muestra por consola.
    
    Args:
        productos (list): Lista de objetos Producto a guardar.
        
    Raises:
        FileNotFoundError: Si el archivo 'docs/productos.dat' no existe.
        pickle.UnpicklingError: Si hay un error al deserializar los datos.
    """

    if productos.__len__() == 0:
        print("No hay productos en el inventario")
        return

    if ruta == 'docs/export.dat':
        print('Se guardará el archivo en la ruta por defecto: export.dat')
        opcion = input("Desea cambiar la ruta? (s/n) -> ")
        if opcion.lower() == 's':
            while True:
                ruta= input("Ingrese la ruta del archivo -> ")
                if validar_ruta(ruta) and ruta != '':
                    break
                 

    manipular_archivo(ruta, productos, 'wb')
    print("Productos guardados correctamente")

def agregar_producto(productos, Producto : Producto):
    """
    Agrega un nuevo producto al archivo de almacenamiento.
    
    Lee la lista actual de productos, agrega el nuevo producto y guarda
    la lista actualizada en el archivo.
    
    Args:
        Producto (Producto): Objeto Producto a agregar al almacenamiento.
        
    Returns:
        Producto: El objeto Producto que fue agregado.
        
    Raises:
        FileNotFoundError: Si el archivo 'docs/productos.dat' no existe.
        pickle.UnpicklingError: Si hay un error al deserializar los datos.
        pickle.PicklingError: Si hay un error al serializar los datos.
    """
    productos.append(Producto)  
    manipular_archivo('docs/productos.dat', productos)
    print("Producto agregado correctamente")
    return productos
