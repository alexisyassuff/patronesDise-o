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


class Director:
    def __init__(self, estrategia: EstrategiaOrdenamiento):
        self.estrategia = estrategia

    def set_estrategia(self, estrategia):
        self.estrategia = estrategia

    def ordenar_datos(self, datos):
        return self.estrategia.ordenar(datos)


# Cliente
if __name__ == "__main__":
    datos = ["banana", "manzana", "kiwi", "frutilla"]

    director = Director(OrdenarAscendente())
    print("Ascendente:", director.ordenar_datos(datos))

    director.set_estrategia(OrdenarDescendente())
    print("Descendente:", director.ordenar_datos(datos))

    director.set_estrategia(OrdenarPorLongitud())
    print("Por longitud:", director.ordenar_datos(datos))
