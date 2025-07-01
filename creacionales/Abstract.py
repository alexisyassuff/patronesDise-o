# Abstract Factory
class FabricaMuebles:
    def crear_silla(self):
        pass

    def crear_mesa(self):
        pass

# Productos abstractos


class Silla:
    def sentarse(self):
        pass


class Mesa:
    def poner_objetos(self):
        pass


# Productos concretos - Modernos
class SillaModerna(Silla):
    def sentarse(self):
        return "Sentado en una silla moderna de metal."


class MesaModerna(Mesa):
    def poner_objetos(self):
        return "Objetos puestos sobre una mesa moderna de vidrio."


# Productos concretos - Vintage
class SillaVintage(Silla):
    def sentarse(self):
        return "Sentado en una silla vintage de madera tallada."


class MesaVintage(Mesa):
    def poner_objetos(self):
        return "Objetos puestos sobre una mesa vintage de roble."


# Fábricas concretas
class FabricaModerna(FabricaMuebles):
    def crear_silla(self):
        return SillaModerna()

    def crear_mesa(self):
        return MesaModerna()


class FabricaVintage(FabricaMuebles):
    def crear_silla(self):
        return SillaVintage()

    def crear_mesa(self):
        return MesaVintage()

# Cliente


def usar_muebles(fabrica: FabricaMuebles):
    silla = fabrica.crear_silla()
    mesa = fabrica.crear_mesa()

    print(silla.sentarse())
    print(mesa.poner_objetos())


if __name__ == "__main__":
    print("Estilo moderno:")
    usar_muebles(FabricaModerna())

    print("\nEstilo vintage:")
    usar_muebles(FabricaVintage())
