from abc import ABC, abstractmethod

# Target


class Impresora(ABC):
    @abstractmethod
    def imprimir(self, mensaje):
        pass

# Adaptee: clase antigua con interfaz incompatible


class ImpresoraVieja:
    def print_texto(self, texto):
        print(f"[Impresora vieja]: {texto}")

# Adapter: adapta ImpresoraVieja a la interfaz esperada


class ImpresoraAdapter(Impresora):
    def __init__(self, impresora_vieja):
        self.impresora_vieja = impresora_vieja

    def imprimir(self, mensaje):
        # Traduce la llamada
        self.impresora_vieja.print_texto(mensaje)

# Cliente


def cliente(impresora: Impresora):
    impresora.imprimir("¡Hola desde el sistema!")


# Uso
if __name__ == "__main__":
    vieja = ImpresoraVieja()
    adaptador = ImpresoraAdapter(vieja)

    cliente(adaptador)
