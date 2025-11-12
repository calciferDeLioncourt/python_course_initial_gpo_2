'''
    POO & PAtterns
'''

class Producto:
    '''Clase que representa un producto con un nombre'''

    def __init__(self, nombre: str):
        '''Constructor de la clase Producto'''
        self._nombre = nombre
    
    @property
    def nombre(self) -> str:
        '''Metodo para obtener el nombre'''
        return self._nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre: str) -> None:
        '''Mtodo para cambiar el nombre'''
        if(len(nuevo_nombre) < 1):
            raise ValueError("El nombre no puede estar vacio")
        self._nombre = nuevo_nombre


producto = Producto("Lap")

print(f"El nombre del producto es: {producto.nombre}")

producto.nombre = ""

print(f"El nombre del producto es: {producto.nombre}")