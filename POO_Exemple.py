# Definim la classe pare
from venv import CORE_VENV_DEPS

import self

class Cotxe:
    def __init__(self, tipus_motor, combustible, portes):
        self.tipus_motor = tipus_motor
        self.combustible = combustible
        self.portes = portes

    def get_tipus_motor(self):
        print(f"El tipus de motor és: {self.tipus_motor}")

    def get_combustible(self):
        print(f"El combustible és : {self.combustible}")

    def get_portes(self):
        print(f"Té {self.portes} portes")

    def set_portes(self, numero_portes):
        self.portes=numero_portes

class Mercedes(Cotxe):
    def __init__(self, tipus_acabat):
        self.tipus_acabat=tipus_acabat

    def tipus_acabat(self):
        print(f"El tipus d'acabat del Mercedes és: {self.tipus_acabat()}")

class Audi(Cotxe):
    def __init__(self, CV,Longitud,Amplada,tipus_motor, combustible, portes):
        self.CV= CV
        self.Longitud=Longitud
        self.Amplada=Amplada
        self.tipus_motor = tipus_motor
        self.combustible = combustible
        self.portes = portes
    def CV(self):
        print(f"Els CV del Audi són: {self.CV()}")
    def Longitud(self):
        print(f"La longitud del Audi és de : {self.Longitud()}")
    def Amplada(self):
        print(f"L'amplada del Audi és de : {self.Amplada()}")

cotxe1=Cotxe("combustió", "gasoil", "5")
cotxe_audi=Audi("200","5","2","combustió","gasoil","5")
cotxe_audi.get_portes()
cotxe1.get_portes()

cotxe_mercedes=Mercedes("Luxury")
cotxe_mercedes.set_portes("4")
cotxe_mercedes.get_portes()
