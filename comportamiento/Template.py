from abc import ABC, abstractmethod

# Clase abstracta (Template)


class GeneradorReporte(ABC):
    def generar(self):
        self.conectar()
        self.extraer_datos()
        self.formatear()
        self.exportar()

    def conectar(self):
        print("Conectando a la base de datos...")

    @abstractmethod
    def extraer_datos(self):
        pass

    @abstractmethod
    def formatear(self):
        pass

    def exportar(self):
        print("Exportando el reporte en PDF.\n")

# Subclases concretas


class ReporteVentas(GeneradorReporte):
    def extraer_datos(self):
        print("Extrayendo datos de ventas...")

    def formatear(self):
        print("Formateando reporte de ventas...")


class ReporteInventario(GeneradorReporte):
    def extraer_datos(self):
        print("Extrayendo datos de inventario...")

    def formatear(self):
        print("Formateando reporte de inventario...")


# Cliente
if __name__ == "__main__":
    print("Generando Reporte de Ventas")
    ventas = ReporteVentas()
    ventas.generar()

    print("Generando Reporte de Inventario")
    inventario = ReporteInventario()
    inventario.generar()
