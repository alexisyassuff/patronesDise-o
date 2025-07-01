from abc import ABC, abstractmethod

# Interfaz común


class Archivo(ABC):
    @abstractmethod
    def abrir(self):
        pass

# Objeto real


class ArchivoReal(Archivo):
    def __init__(self, nombre):
        self.nombre = nombre

    def abrir(self):
        print(f"Abrir archivo real: {self.nombre}")

# Proxy


class ProxyArchivo(Archivo):
    def __init__(self, nombre, usuario):
        self.nombre = nombre
        self.usuario = usuario
        self.archivo_real = None

    def abrir(self):
        if self.usuario == "admin":
            if self.archivo_real is None:
                self.archivo_real = ArchivoReal(self.nombre)
            self.archivo_real.abrir()
        else:
            print(
                f"Acceso denegado a '{self.nombre}' para el usuario '{self.usuario}'.")


if __name__ == "__main__":
    archivo1 = ProxyArchivo("datos_confidenciales.txt", "admin")
    archivo1.abrir()

    archivo2 = ProxyArchivo("datos_confidenciales.txt", "invitado")
    archivo2.abrir()
