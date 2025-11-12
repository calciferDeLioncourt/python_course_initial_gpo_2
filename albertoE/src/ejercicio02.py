# Funciones
def saludar() -> None:
    '''Función que imprime un saludo en pantalla.'''
    print("¡Hola, nundo!")

saludar()

def saludar(nombre: str) -> None:
    '''Función que imprime un saludo personalizado.'''
    print(f"¡Hola, {nombre}!")

saludar("Alberto")

'''
    Lambdas
'''
sumar = lambda num_1, num_2: num_1 + num_2
resultado = sumar(5, 3)
print(f"La suma es: {resultado}")

'''
    Maps
'''
list_data = range(5)
operacion = lambda num_1: num_1 **2
resultado = map(operacion, list_data)
print(list(resultado))
# print(list(map(lambda num_1: num_1 **2, range(5))))


'''
    Filters
'''
print(list(filter(lambda x: x % 2 == 0, range(10))))



