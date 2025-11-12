class Procesador:
    def __init__(self, marca:str, nucleos: int):
        self.marca = marca
        self.nucleos = nucleos

class Memoria:
    def __init__(self, tamano: int, velocidad: float):
        self.tamano = tamano
        self.velocidad = velocidad

class Computadora:
    def __init__(self, procesador: Procesador, memoria: Memoria):
        self.procesador = procesador
        self.memoria = memoria

    def descripcion(self):
        print('****************')
        print("Procesador")
        print(f"Marca: {self.procesador.marca}")
        print(f"Nucleos: {self.procesador.nucleos}")
        print("Memoria")
        print(f"Tamaño: {self.memoria.tamano}")
        print(f"Velocidad: {self.memoria.velocidad}")
        print('****************')


compu = Computadora(
    procesador=Procesador('Intel', 8),
    memoria=Memoria('Kingston', 2700)
)

print(compu.descripcion())
