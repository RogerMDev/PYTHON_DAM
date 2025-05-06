class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def encender(self):
        print(f"El motor {self.tipo} de {self.potencia}CV se ha encendido.")


class Coche:
    def __init__(self, marca, modelo, ano, tipo_motor, potencia_motor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motor = Motor(tipo_motor, potencia_motor)  # Composición

    def arrancar(self):
        print(f"{self.marca} {self.modelo} ({self.ano}) está arrancando...")
        self.motor.encender()

    def detener(self):
        print(f"{self.marca} {self.modelo} se ha detenido.")


# Ejemplo de uso
mi_coche = Coche("Toyota", "Corolla", 2020, "Gasolina", 132)
mi_coche.arrancar()
mi_coche.detener()
