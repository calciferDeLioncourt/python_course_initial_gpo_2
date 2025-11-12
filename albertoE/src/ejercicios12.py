'''
    inyeccion de dependencias
'''
from abc import ABC, abstractmethod
 
 
#inyeccion por constructor
class ServiceEmail:
    def enviar_email(self, mensaje):
        print(f"Enviar email - {mensaje}")

class Notificador: 
    def __init__(self, service:ServiceEmail):
        self.service = service

    def notificar( self, mensaje):
        self.service.enviar_email(mensaje)

service_email = ServiceEmail()
notifica = Notificador(service=service_email)

notifica.notificar("Contenido")

#inyeccion por setter
class ServiceEmail:
    def enviar_email(self, mensaje):
        print(f"Email enviado - {mensaje}")

class Notificador: 
    def set_email_service(self, service_email: ServiceEmail):
        self.service = service_email
    
    def notificar( self, mensaje):
        self.service.enviar_email(mensaje)



class MotorBase(ABC):
    @abstractmethod
    def encender(self):
        pass

class MotorElectrico(MotorBase):
    def encender(self):
        print("Encendido electrico")

class Auto:
    def __init__(self, motor_base: MotorBase):
        self.motor = motor_base

    def arrancar(self):
        self.motor.encender

auto = Auto(MotorElectrico())
auto.arrancar()