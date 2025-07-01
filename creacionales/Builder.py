# Interfaces del patrón
class Computadora:
    def __init__(self):
        self.ram = None
        self.ssd = None
        self.procesador = None

    def mostrar_especificaciones(self):
        print(f"RAM: {self.ram}")
        print(f"SSD: {self.ssd}")
        print(f"Procesador: {self.procesador}")


class BuilderComputadora:
    def agregar_ram(self, ram):
        pass

    def agregar_ssd(self, ssd):
        pass

    def agregar_procesador(self, procesador):
        pass

    def obtener_resultado(self):
        pass

# Constructores concretos


class BuilderOficina(BuilderComputadora):
    def __init__(self):
        self.computadora = Computadora()

    def agregar_ram(self, ram):
        self.computadora.ram = ram

    def agregar_ssd(self, ssd):
        self.computadora.ssd = ssd

    def agregar_procesador(self, procesador):
        self.computadora.procesador = procesador

    def obtener_resultado(self):
        return self.computadora


class BuilderGamer(BuilderComputadora):
    def __init__(self):
        self.computadora = Computadora()

    def agregar_ram(self, ram):
        self.computadora.ram = ram

    def agregar_ssd(self, ssd):
        self.computadora.ssd = ssd

    def agregar_procesador(self, procesador):
        self.computadora.procesador = procesador

    def obtener_resultado(self):
        return self.computadora


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construir(self, ram, ssd, procesador):
        self.builder.agregar_ram(ram)
        self.builder.agregar_ssd(ssd)
        self.builder.agregar_procesador(procesador)


if __name__ == "__main__":
    print("=== Construyendo computadora de oficina ===")
    builder_oficina = BuilderOficina()
    director_oficina = Director(builder_oficina)
    director_oficina.construir(
        ram="8GB",
        ssd="256GB",
        procesador="Intel i5"
    )
    computadora_oficina = builder_oficina.obtener_resultado()
    computadora_oficina.mostrar_especificaciones()

    print("\n=== Construyendo computadora gamer ===")
    builder_gamer = BuilderGamer()
    director_gamer = Director(builder_gamer)

    # El usuario decide qué componentes quiere
    ram_usuario = "32GB"
    ssd_usuario = "1TB"
    procesador_usuario = "Ryzen 7"

    director_gamer.construir(
        ram=ram_usuario,
        ssd=ssd_usuario,
        procesador=procesador_usuario
    )
    computadora_gamer = builder_gamer.obtener_resultado()
    computadora_gamer.mostrar_especificaciones()
