# Interfaz del manejador
class ManejadorAyuda:
    def establecer_sucesor(self, sucesor):
        pass

    def manejar_ayuda(self, problema):
        pass

# Manejadores concretos


class SoporteBasico(ManejadorAyuda):
    def __init__(self):
        self.sucesor = None

    def establecer_sucesor(self, sucesor):
        self.sucesor = sucesor

    def manejar_ayuda(self, problema):
        if problema == "contraseña":
            print("Soporte Básico: Problema de contraseña resuelto.")
        elif self.sucesor:
            self.sucesor.manejar_ayuda(problema)
        else:
            print("Soporte Básico: No se pudo resolver el problema.")


class SoporteTecnico(ManejadorAyuda):
    def __init__(self):
        self.sucesor = None

    def establecer_sucesor(self, sucesor):
        self.sucesor = sucesor

    def manejar_ayuda(self, problema):
        if problema == "wifi":
            print("Soporte Técnico: Problema de conexión WiFi resuelto.")
        elif self.sucesor:
            self.sucesor.manejar_ayuda(problema)
        else:
            print("Soporte Técnico: No se pudo resolver el problema.")


class SoporteInstitucional(ManejadorAyuda):
    def __init__(self):
        self.sucesor = None

    def establecer_sucesor(self, sucesor):
        self.sucesor = sucesor

    def manejar_ayuda(self, problema):
        if problema == "pago":
            print("Soporte Institucional: Problema de pago resuelto.")
        elif self.sucesor:
            self.sucesor.manejar_ayuda(problema)
        else:
            print("Soporte Institucional: No se pudo resolver el problema.")


if __name__ == "__main__":
    soporte_basico = SoporteBasico()
    soporte_tecnico = SoporteTecnico()
    soporte_institucional = SoporteInstitucional()

    soporte_basico.establecer_sucesor(soporte_tecnico)
    soporte_tecnico.establecer_sucesor(soporte_institucional)

    cliente = soporte_basico

    print("➡️ Cliente: Olvidé mi contraseña.")
    cliente.manejar_ayuda("contraseña")

    print("\n➡️ Cliente: No tengo WiFi.")
    cliente.manejar_ayuda("wifi")

    print("\n➡️ Cliente: Tengo problemas con el pago.")
    cliente.manejar_ayuda("pago")

    print("\n➡️ Cliente: Tengo un problema desconocido.")
    cliente.manejar_ayuda("otra cosa")
