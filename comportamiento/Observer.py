# Interfaz Observer
class Observador:
    def actualizar(self, temperatura):
        pass

# Sujeto


class EstacionMeteorologica:
    def __init__(self):
        self._observadores = []
        self._temperatura = 0

    def agregar(self, observador):
        self._observadores.append(observador)

    def quitar(self, observador):
        self._observadores.remove(observador)

    def notificar(self):
        for obs in self._observadores:
            obs.actualizar(self._temperatura)

    def set_temperatura(self, nueva_temp):
        print(f"\nTemperatura actualizada a {nueva_temp}°C")
        self._temperatura = nueva_temp
        self.notificar()

# Observadores concretos


class PantallaLCD(Observador):
    def actualizar(self, temperatura):
        print(f"[LCD] Mostrando nueva temperatura: {temperatura}°C")


class Alarma(Observador):
    def actualizar(self, temperatura):
        if temperatura > 30:
            print("[ALARMA] ¡Temperatura alta!")
        else:
            print("[ALARMA] Temperatura normal.")

# Cliente


def cliente():
    estacion = EstacionMeteorologica()
    lcd = PantallaLCD()
    alarma = Alarma()

    estacion.agregar(lcd)
    estacion.agregar(alarma)

    estacion.set_temperatura(25)
    estacion.set_temperatura(35)


if __name__ == "__main__":
    cliente()
