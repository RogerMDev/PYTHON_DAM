import random
import time

class Cotxe:
    def __init__(self, nom, marca, velocitat, acceleracio, resistencia):
            self.nom = nom
            self.marca = marca
            self.velocitat = velocitat
            self.acceleracio = acceleracio
            self.resistencia = resistencia

    def accelerar(self):
            self.velocitat+= self.acceleracio
            print(f"{self.nom} accelera! Nova velocitat: {self.velocitat} km/h!")

    def rebre_dany(self,dany):
        self.resistencia -= dany
        print(f"{self.nom} ha rebut {dany} de dany! Resistència restant: {self.resistencia}")
        if self.resistencia <= 0:
            print(f"{self.nom} ha quedat destruït!")

    def esta_actiu(self):
        return self.resistencia > 0

    def frenar(self):
            self.velocitat -= self.acceleracio
            if self.velocitat <0:
                self.velocitat = 0
            print(f"{self.nom} frena! Velocitat actual: {self.velocitat} km/h!")

    def __str__(self):
        return f"{self.nom} ({self.marca}) - Velocitat: {self.velocitat} km/h - Resistència: {self.resistencia}"

class CircuitCurses:
    def __init__(self, nom):
            self.nom = nom
            self.cotxes = []

    def afegir_cotxe(self,cotxe):
        self.cotxes.append(cotxe)
        print(f"{cotxe.nom} ha estat afegit a la cursa!")

    def iniciar_carrera(self):
        print(f"\n Iniciant la cursa al circuit {self.nom}! ")
        while len([c for c in self.cotxes if c.esta_actiu()]) > 1:
            print("\n Nova volta!")
            for cotxe in self.cotxes:
                if cotxe.esta_actiu():
                    cotxe.accelerar()
                    if random.random() < 0.3:  # Probabilitat del 30% de xocar
                        dany = random.randint(10, 30)
                        cotxe.rebre_dany(dany)
            time.sleep(1)

        guanyador = next((c for c in self.cotxes if c.esta_actiu()), None)
        if guanyador:
            print(f"\n {guanyador.nom} ha guanyat la cursa! ")
        else:
            print("\n Tots els cotxes han estat destruïts! No hi ha guanyador!")


class Esportiu(Cotxe):
    def __init__(self, nom, marca):
        super().__init__(nom, marca, velocitat=100, acceleracio=20, resistencia=50)


class TotTerreny(Cotxe):
    def __init__(self, nom, marca):
        super().__init__(nom, marca, velocitat=80, acceleracio=10, resistencia=100)


class Classic(Cotxe):
    def __init__(self, nom, marca):
        super().__init__(nom, marca, velocitat=90, acceleracio=15, resistencia=75)


cotxe1 = Cotxe("Cotxe 1", "Marca Cotxe 1", 30,5 ,100)

# Exemple d'ús
circuit = CircuitCurses("Montecarlo")
cotxe1 = Esportiu("Ferrari F8", "Ferrari")
cotxe2 = TotTerreny("Jeep Wrangler", "Jeep")
cotxe3 = Classic("Ford Mustang", "Ford")

circuit.afegir_cotxe(cotxe1)
circuit.afegir_cotxe(cotxe2)
circuit.afegir_cotxe(cotxe3)

circuit.iniciar_carrera()



