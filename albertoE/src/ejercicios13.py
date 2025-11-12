class Contenedor:
    def __init__(self):
        self.registro ={}

    def registrar(self, nombre, proveedor):
        self.registro[nombre] = proveedor

    def resolver(self, nombre):
        return self.registro[nombre]()
    
class Logger:
    def info(self, mensaje):
        print(f"[INFO] {mensaje}")

class Servicio:
    def __init__(self, logger):
        self.logger = logger

    def procesar_data(self):
        self.logger.info('Prosesando data...')

container = Contenedor()

container.registrar("logger", Logger)
container.registrar("service", lambda: Servicio(container.resolver("logger")))

service = container.resolver("service")

service.procesar_data()