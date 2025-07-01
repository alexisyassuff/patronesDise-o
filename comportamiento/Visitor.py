from abc import ABC, abstractmethod

# Interfaz Visitor


class Visitor(ABC):
    @abstractmethod
    def visit_archivo(self, archivo):
        pass

    @abstractmethod
    def visit_carpeta(self, carpeta):
        pass

# Interfaz Elemento


class ElementoSistema(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Elemento concreto


class Archivo(ElementoSistema):
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño

    def accept(self, visitor):
        visitor.visit_archivo(self)

# Otro elemento concreto


class Carpeta(ElementoSistema):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def accept(self, visitor):
        visitor.visit_carpeta(self)

# Visitor concreto


class CalculadorTamaño(Visitor):
    def __init__(self):
        self.total = 0

    def visit_archivo(self, archivo):
        self.total += archivo.tamaño

    def visit_carpeta(self, carpeta):
        for elemento in carpeta.elementos:
            elemento.accept(self)


# Cliente
if __name__ == "__main__":
    archivo1 = Archivo("doc.txt", 100)
    archivo2 = Archivo("foto.jpg", 300)
    carpeta = Carpeta("Mis Documentos")
    carpeta.agregar(archivo1)
    carpeta.agregar(archivo2)

    visitante = CalculadorTamaño()
    carpeta.accept(visitante)

    print(f"Tamaño total: {visitante.total} KB")
