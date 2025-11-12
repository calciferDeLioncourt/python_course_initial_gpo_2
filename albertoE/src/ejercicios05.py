'''
    Manejo de errores y logging
'''

class CustomError(Exception):
    '''Excepción personalizada para manejo específico de errores.'''
    pass

def funcion_con_error(n1: int):
    if(n1 < 0):
        raise CustomError("Error: El número no puede ser negativo.")
    print('El numero es correcto')

try:
    funcion_con_error(5)
except Exception as e:
    print(f"error: {e}")
else:
    print(f"ejecución correcta")
finally:
    print("Ejecución finalizada.")