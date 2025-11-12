from dependency_injector import containers, providers

class Logger:
    def info(self, mensaje):
        print(f"[INFO] {mensaje}")

class Servicio:
    def __init__(self, logger):
        self.logger = logger

    def procesar_data(self):
        self.logger.info("Procesar data...")

class Container( containers.DeclarativeContainer ):
    logger = providers.Singleton(Logger)
    service = providers.Factory(Servicio, logger=logger)

container = Container()

service= container.service()

service.procesar_data()
