# Ejercicio 4: Polimorfismo
# Implementa polimorfismo sobrescribiendo métodos en clases hijas.
# Requisitos:
# 1. Crea una clase base 'Animal' con un método 'hacer_sonido()'.
# 2. Crea dos subclases 'Perro' y 'Gato' que sobrescriban el método 'hacer_sonido()' con diferentes sonidos.
# 3. Crea una función que acepte cualquier objeto 'Animal' y llame a su método 'hacer_sonido()'.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "El animal hace un sonido"

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)  # Llamamos al constructor de la clase base

    def hacer_sonido(self):
        return "Guau, Guau, Guau !!"

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)  # Llamamos al constructor de la clase base

    def hacer_sonido(self):
        return "Miau, Miau, Miau !!"

# Función que acepta cualquier objeto Animal
def hacer_sonido_del_animal(animal):
    print(f"El sonido de {animal.nombre} es: {animal.hacer_sonido()}")

perro = Perro("Rex")
gato = Gato("Whiskers")
perro2 = Perro("Toby")

hacer_sonido_del_animal(perro)
hacer_sonido_del_animal(gato)
hacer_sonido_del_animal(perro2)
