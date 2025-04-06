

# Objetivo: Crear una clase Personaje y usarla para crear objetos.
# 1. Define una clase Personaje con los atributos nombre y nivel.
# 2. Define un método saludar que imprima un saludo incluyendo el nombre y nivel del personaje.
# 3. Crea dos objetos de la clase Personaje y llama al método saludar para cada uno.

class Personaje:

    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

    def saludar(self):
        print (f"Hola me llamo {self.nombre} y tengo nivel {self.nivel}.")

personaje1 = Personaje("Roger",55)
personaje2 = Personaje("Fernando", 100)

personaje1.saludar()
personaje2.saludar()

