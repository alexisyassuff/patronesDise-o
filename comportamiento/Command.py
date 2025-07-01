from abc import ABC, abstractmethod

# Command


class Comando(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

# Receptor


class Luz:
    def encender(self):
        print("Luz encendida")

    def apagar(self):
        print("Luz apagada")

# ConcreteCommands


class EncenderLuz(Comando):
    def __init__(self, luz):
        self.luz = luz

    def ejecutar(self):
        self.luz.encender()


class ApagarLuz(Comando):
    def __init__(self, luz):
        self.luz = luz

    def ejecutar(self):
        self.luz.apagar()

# Invocador


class ControlRemoto:
    def __init__(self):
        self.boton = None

    def establecer_comando(self, comando):
        self.boton = comando

    def presionar_boton(self):
        if self.boton:
            self.boton.ejecutar()


if __name__ == "__main__":
    luz_sala = Luz()

    comando_encender = EncenderLuz(luz_sala)
    comando_apagar = ApagarLuz(luz_sala)

    control = ControlRemoto()

    control.establecer_comando(comando_encender)
    control.presionar_boton()

    control.establecer_comando(comando_apagar)
    control.presionar_boton()
