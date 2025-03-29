import UI as ui
from utils.validar_input import validar_input

# Clase Producto
class Producto:
    def __init__(self, codigo : None, nombre : None, precio : None, cantidad : None):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        if codigo is None:
            ui.imprimir_titulo("Agregar producto")
            while self.codigo is None or self.codigo == "":
                self.codigo = input("Ingrese el código del producto: ")
        if nombre is None:
            while self.nombre is None or self.nombre == "":
                self.nombre = input("Ingrese el nombre del producto: ")
        if precio is None:
            while True:
                precio_str = validar_input(
                    "Ingrese el precio del producto: ",
                    expresion_regular=r"^\d*\.?\d+$",
                    mensaje_error="Por favor ingrese un número válido (ejemplo: 10.50)"
                )
                try:
                    self.precio = float(precio_str)
                    if self.precio > 0:
                        break
                    print("El precio debe ser mayor a 0")
                except ValueError:
                    print("Error al convertir el precio. Intente nuevamente.")
        if cantidad is None:
            while True:
                cantidad_str = validar_input(
                    "Ingrese la cantidad del producto: ",
                    expresion_regular=r"^\d+$",
                    mensaje_error="Por favor ingrese un número entero positivo"
                )
                try:
                    self.cantidad = int(cantidad_str)
                    if self.cantidad > 0:
                        break
                    print("La cantidad debe ser mayor a 0")
                except ValueError:
                    print("Error al convertir la cantidad. Intente nuevamente.")
    
    def __str__(self):
        return f"\n{self.codigo} - {self.nombre} - ${self.precio} - {self.cantidad}\n"
    