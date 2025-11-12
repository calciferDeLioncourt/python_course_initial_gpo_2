'''
    Args y Kwargs
'''
#args: argumentos posicionales
import time


def procesar_datos(*args) -> None:
    print(f"Argumentos posicionales recibidos: {args}")
    # for indice, valor in enumerate(args):
    #     print(f"Argumento {indice}: {valor}")
mi_tupla = (2,3,4)
# procesar_datos(2,3,4)

#kwargs: argumentos nombrados
def saludos_dinamicos(**kwargs) -> None:
    print(f"Argumentos nombrados recibidos: {kwargs}")

# saludos_dinamicos(nombre="Alberto", edad=30)

# Generadores -> para manejar grandes volúmenes de datos, utilizan yield en lugar de return

def generador_datos(limite: int):
    '''Generador que produce números hasta un límite dado.'''
    print("Iniciando el generador...")
    for num in range(limite):
        print(f"Bucle en posición: {num}")
        yield num
    print("Generador finalizado.")

def generador_datos_tradicional(limite: int) -> list:
    '''Funcion que produce números hasta un límite dado.'''
    print("Iniciando el funcion...")
    res = []
    for num in range(limite):
        print(f"Bucle en posición: {num}")
        res.append(num)
    return res
    print("funcion finalizado.")

print("Usando el generador de números:")
print(type(generador_datos))
gen = generador_datos(5)

for item in gen:
    print(f"Número generado: {item}")

listaa = generador_datos_tradicional(5)

for item in listaa:
    print(f"Número generado: {item}")

'''
    Generador de Fibonacci
'''
 
def fibonacci(cantidad: int):
    '''
    Generador que produce números de la serie de Fibonacci.
    
    Args:
        cantidad (int): Cantidad de números de Fibonacci a generar
        
    Yields:
        int: El siguiente número en la serie de Fibonacci
    '''
    a:int = 1 
    b:int = 1
    contador: int = 0
    
    while contador < cantidad:
        yield a
        a, b = b, a + b
        contador += 1


print("\n--- Serie de Fibonacci usando Generador ---")
print("Primeros 10 números de Fibonacci:")
for numero in fibonacci(10):
    print(numero, end=" ")

'''
    Decoradores -> Aumentar funcionalidad sin modificar la funcion original
'''



def decorador(func):
    def envoltura():
        print("\ninicio dec ")
        func()
        print("final")
    return envoltura

@decorador
def saludar():
    print("Hola, mundo!")

saludar()

#decorador con args y kwargs

# def decorador(func):
#     def envoltura(*args, **kwargs):
#         print(f"Inicio con args {args} y kwargs {kwargs}")
#         func(*args, **kwargs)
#         print("Final dec")
#     return envoltura
