from abc import ABC, abstractmethod

# Componente


class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

# Componente concreto


class NotificadorBasico(Notificador):
    def enviar(self, mensaje):
        print(f"[EMAIL] Enviando mensaje: {mensaje}")

#  Decorador base


class NotificadorDecorador(Notificador):
    def __init__(self, envoltorio):
        self.envoltorio = envoltorio

    def enviar(self, mensaje):
        self.envoltorio.enviar(mensaje)

#  Decorador concreto: SMS


class NotificadorSMS(NotificadorDecorador):
    def enviar(self, mensaje):
        super().enviar(mensaje)
        print(f"[SMS] Enviando mensaje: {mensaje}")

#  Decorador concreto: Log


class NotificadorLogger(NotificadorDecorador):
    def enviar(self, mensaje):
        super().enviar(mensaje)
        print(f"[LOG] Mensaje enviado: '{mensaje}'")

#  Cliente


def cliente():
    print("Notificación básica:")
    basico = NotificadorBasico()
    basico.enviar("Hola mundo")

    print("\nNotificación con SMS:")
    con_sms = NotificadorSMS(basico)
    con_sms.enviar("Hola mundo")

    print("\nNotificación con SMS y Log:")
    full = NotificadorLogger(con_sms)
    full.enviar("Hola mundo")


#  Ejecutar
if __name__ == "__main__":
    cliente()
