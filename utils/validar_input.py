import re
def validar_input(input_usuario: str, expresion_regular: str = None, mensaje_error: str = None) -> str:
    """
    Valida la entrada del usuario opcionalmente con una expresión regular.
    
    Args:
        input_usuario (str): Mensaje que se mostrará al usuario
        expresion_regular (str, opcional): Patrón de expresión regular para validar
        mensaje_error (str, opcional): Mensaje personalizado de error
        
    Returns:
        str: Entrada válida del usuario
    """
    while True:
        try:
            ingreso = input(input_usuario)
            
            # Si no hay expresión regular, retorna el input directamente
            if not expresion_regular:
                return ingreso
            
            # Valida la entrada con la expresión regular
            if re.match(expresion_regular, ingreso):
                return ingreso
            else:
                print(mensaje_error or "Entrada no válida. Intente nuevamente.")
                
        except ValueError:
            print("Error en la entrada. Intente nuevamente.")

