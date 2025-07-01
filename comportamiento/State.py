from abc import ABC, abstractmethod

# State (Interfaz)


class EstadoImpresora(ABC):
    @abstractmethod
    def manejar(self, impresora):
        pass

# Estados concretos


class Lista(EstadoImpresora):
    def manejar(self, impresora):
        print("Impresora lista. Comenzando a imprimir...")
        impresora.set_estado(Imprimiendo())


class Imprimiendo(EstadoImpresora):
    def manejar(self, impresora):
        print("Ya está imprimiendo. Terminando impresión...")
        impresora.set_estado(SinPapel())


class SinPapel(EstadoImpresora):
    def manejar(self, impresora):
        print("No hay papel. Por favor, recargue.")
        # No cambia de estado automáticamente

# Contexto


class Impresora:
    def __init__(self):
        self.estado = Lista()

    def set_estado(self, estado):
        self.estado = estado

    def ejecutar(self):
        self.estado.manejar(self)


# Cliente
if __name__ == "__main__":
    impresora = Impresora()

    impresora.ejecutar()  # Lista -> Imprimiendo
    impresora.ejecutar()  # Imprimiendo -> SinPapel
    impresora.ejecutar()
