import Producto
def imprimir_menu(message=None):
    print("\n"*3)
    if message:
        for m in message:
            print(m)
    print("*"+"-"*48+"*")
    print("|"+"Bienvenido al sistema de inventario".center(48)+"|")
    print("*"+"-"*48+"*")
    print("|"+"Seleccione una opción".center(48)+"|")
    print("|"+"".center(48)+"|")
    print("|"+"    1. Agregar producto".ljust(48)+"|")
    print("|"+"    2. Buscar producto".ljust(48)+"|")
    print("|"+"    3. Listar productos".ljust(48)+"|")
    print("|"+"    4. Valor inventario productos".ljust(48)+"|")
    print("|"+"    5. Guardar en disco".ljust(48)+"|")
    print("|"+"    6. Cargar documento".ljust(48)+"|")
    print("|"+"    0. Salir".ljust(48)+"|")
    print("*"+"-"*48+"*")


def imprimir_titulo(title):
    print("\n"*3)
    print("*"+"-"*48+"*")
    print("|"+f"{title}".center(48)+"|")
    print("*"+"-"*48+"*")

def imprimir_producto(producto : Producto):
    print("\n"*1)
    print("*"+"-"*48+"*")
    print("|"+f"Producto: {producto.nombre}".center(48)+"|")
    print("*"+"-"*48+"*")
    print("|"+"Código: "+str(producto.codigo).ljust(40)+"|")
    print("|"+"Nombre: "+f"{producto.nombre}".ljust(40)+"|")
    print("|"+"Precio: "+str(producto.precio).ljust(40)+"|")
    print("|"+"Cantidad: "+str(producto.cantidad).ljust(38)+"|")
    print("*"+"-"*48+"*")
    print("\n"*2)