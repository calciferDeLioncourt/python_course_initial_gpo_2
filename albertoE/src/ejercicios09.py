'''
    modelado de objetos mediante composicion y herencia
'''

from dataclasses import dataclass


@dataclass
class Motor:
    tipo: str

@dataclass
class Rueda:
    tamano: int

@dataclass
class Coche:
    marca: str
    motor: Motor
    ruedas: list[Rueda]
    
    def __str__(self):
        return(f"\nCoche marca: {self.marca}"
            f"\nTipo de motor: {self.motor.tipo}"
            f"\nRuedas: {len(self.ruedas)}")

auto_uno = Coche(
    marca="VW",
    motor=Motor('Diesel'),
    ruedas=[Rueda(2), Rueda(2)]
)

print(auto_uno)