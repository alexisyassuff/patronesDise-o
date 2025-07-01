import datetime


class Logger():
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def log(self, mensaje):
        tiempo = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensaje_formateado = f"[{tiempo}] {mensaje}"
        print(mensaje_formateado)


def modulo_usuario():
    logger = Logger()
    print(logger)
    logger.log("Usuario creado correctamente.")


def modulo_prestamo():
    logger = Logger()
    print(logger)
    logger.log("Préstamo registrado.")


if __name__ == "__main__":
    modulo_usuario()
    modulo_prestamo()
