#EJERCICIO 2:
#Objetivo: Crear una clase Arma con atributos y métodos.
#1. Define una clase Arma con los atributos nombre, daño y tipo.
#2. Define un método mostrar_info que devuelva una cadena con la información del arma.
#3. Crea un objeto de la clase Arma y llama al método mostrar_info

#EJERCICIO 3:
#Objetivo: Añadir más métodos a una clase.
#1. Añade un método usar a la clase Arma que imprima "Usando el arma".
#2. Añade un método guardar que imprima "Guardando el arma".
#3. Crea un objeto de la clase Arma y llama a los métodos usar y guardar.

#EJERCICIO 4:
#Objetivo: Usar atributos de clase.
#1. Define un atributo de clase durabilidad en la clase Arma con el valor 100.
#2. Crea dos objetos de la clase Arma y muestra el valor del atributo durabilidad para ambos.

class Arma:
    def __init__(self, nombre, dano, tipo):
        self.nombre = nombre
        self.dano = dano
        self.tipo = tipo
        self.durabilidad = 100

    def mostrar_info(self):
        print(f"El arma {self.nombre}, hace {self.dano} al golpear y es de tipo {self.tipo}.")

    def usar(self):
        print("Usando el arma")

    def guardar(self):
        print("Guardando el arma")

arma1 = Arma("Asesino de dragones", 199, "fuego")
arma2 = Arma("Bastón mágico", 201,"hielo")

arma1.usar()
arma1.mostrar_info()
print(f"La durabilidad de la arma {arma1.nombre} es {arma1.durabilidad}")
arma1.guardar()

arma2.usar()
arma2.mostrar_info()
print(f"La durabilidad de la arma {arma2.nombre} es {arma2.durabilidad}")
arma2.guardar()



