'''
    Herencia y composicion
'''

class Animal():
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Hacer sonido")

class Perro(Animal):
    def __init__(self, nombre="Perro"):
        super().__init__(nombre)    

    def hablar(self):
        print(self.nombre)
        print("guau guau")

# animal = Animal()
perro = Perro()

# animal.hablar()
perro.hablar()