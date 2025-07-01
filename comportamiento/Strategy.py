from abc import ABC, abstractmethod

# Strategy


class EstrategiaOrdenamiento(ABC):
    @abstractmethod
    def ordenar(self, datos):
        pass

# Estrategias concretas


class OrdenarAscendente(EstrategiaOrdenamiento):
    def ordenar(self, datos):
        return sorted(datos)


class OrdenarDescendente(EstrategiaOrdenamiento):
    def ordenar(self, datos):
        return sorted(datos, reverse=True)


class OrdenarPorLongitud(EstrategiaOrdenamiento):
    def ordenar(self, datos):
        return sorted(datos, key=len)

# Contexto


class Ordenador:
    def __init__(self, estrategia: EstrategiaOrdenamiento):
        self.estrategia = estrategia

    def set_estrategia(self, estrategia):
        self.estrategia = estrategia

    def ordenar_datos(self, datos):
        return self.estrategia.ordenar(datos)


# Cliente
if __name__ == "__main__":
    datos = ["banana", "manzana", "kiwi", "frutilla"]

    ordenador = Ordenador(OrdenarAscendente())
    print("Ascendente:", ordenador.ordenar_datos(datos))

    ordenador.set_estrategia(OrdenarDescendente())
    print("Descendente:", ordenador.ordenar_datos(datos))

    ordenador.set_estrategia(OrdenarPorLongitud())
    print("Por longitud:", ordenador.ordenar_datos(datos))
