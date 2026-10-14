# Código con Facade

class Bateria:
    def encender(self):
        print("Batería activada")


class Procesador:
    def iniciar(self):
        print("Procesador iniciado")


class Wifi:
    def activar(self):
        print("Wi-Fi activado")


# Facade: simplifica el encendido del celular.
class CelularFacade:
    def __init__(self):
        self.bateria = Bateria()
        self.procesador = Procesador()
        self.wifi = Wifi()

    def encender_celular(self):
        # La fachada coordina los componentes.
        self.bateria.encender()
        self.procesador.iniciar()
        self.wifi.activar()


# El usuario solo necesita utilizar la fachada.
def main():
    celular = CelularFacade()
    celular.encender_celular()


if __name__ == "__main__":
    main()
