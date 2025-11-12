'''
    ejercicio decoradores
'''

import time


def decorador(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        ejecucion = func(*args, **kwargs)
        fin = time.time()
        print(f"\nTiempo de inicio {inicio}")
        print(f"Tiempo de fin {fin}")
        print(f"Tiempo de ejecución: {fin - inicio} segundos")
        return ejecucion
    return envoltura

@decorador
def funcion_lenta() -> None:
    '''Función que simula una operación lenta.'''
    time.sleep(5)  # Simula una operación que tarda 5 segundos
    print("Función lenta ha terminado.")

funcion_lenta()
