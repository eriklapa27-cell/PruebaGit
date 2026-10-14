# Código sin Facade


class Bateria:
    def encender(self):
        print("Batería activada")


class Procesador:
    def iniciar(self):
        print("Procesador iniciado")


class Wifi:
    def activar(self):
        print("Wi-Fi activado")


# El usuario debe coordinar todos los componentes.
def main():
    bateria = Bateria()
    procesador = Procesador()
    wifi = Wifi()

    bateria.encender()
    procesador.iniciar()
    wifi.activar()


if __name__ == "__main__":
    main()

