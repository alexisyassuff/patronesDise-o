from abc import ABC, abstractmethod

# Componente


class ItemBiblioteca(ABC):
    @abstractmethod
    def mostrar(self, nivel=0):
        pass

# Hoja


class Recurso(ItemBiblioteca):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("  " * nivel + f"- Recurso: {self.nombre}")

# Compuesto


class Categoria(ItemBiblioteca):
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

    def agregar(self, item):
        self.hijos.append(item)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"+ Categoría: {self.nombre}")
        for hijo in self.hijos:
            hijo.mostrar(nivel + 1)

# Cliente


def cliente():
    # Crear recursos
    libro = Recurso("Libro: Python Básico")
    revista = Recurso("Revista: Tech Monthly")

    # Crear categorías
    cat_prog = Categoria("Programación")
    cat_prog.agregar(libro)

    cat_tecno = Categoria("Tecnología")
    cat_tecno.agregar(revista)

    # Subcategoría
    cat_informatica = Categoria("Informática")
    cat_informatica.agregar(cat_prog)
    cat_informatica.agregar(cat_tecno)

    # Mostrar estructura completa
    cat_informatica.mostrar()


# Ejecutar cliente
if __name__ == "__main__":
    cliente()
