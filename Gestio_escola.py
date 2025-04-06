
class Persones:
    def __init__(self, nom, cognom, dni):
        self.nom = nom
        self.cognom = cognom
        self.dni = dni

    def presentar(self):
        print(f"Hola, em dic {self.nom} {self.cognom}.")

class Escola:
    def __init__(self):
        self.estudiants = []
        self.professors = []

    def afegir_estudiants(self, estudiant):
        self.estudiants.append(estudiant)

    def afegir_professors(self, professor):
        self.professors.append(professor)

    def mostrar_persones(self):
        self.mostrar_professors()
        self.mostrar_estudiants()

    def mostrar_estudiants(self):
        print("Estudiants: ")
        for estudiant in self.estudiants:
            estudiant.presentar()

    def mostrar_professors(self):
        print("\nProfessors: ")
        for professor in self.professors:
            professor.presentar()

class Estudiant(Persones):
    def __init__(self, nom, cognom,dni,curs):
        super().__init__(nom, cognom,dni)
        self.curs = curs

    def presentar(self):
        print(f"Soc estudiant de {self.curs}.")

class Professor(Persones):
    def __init__(self, nom, cognom, dni,assignatura ):
        super().__init__(nom, cognom,dni)
        self.assignatura = assignatura

    def presentar(self):
        print(f"Soc professor de {self.assignatura}.")

#Creem instància d'escola
escola = Escola()

#Creem estudiants
Estudiant1 = Estudiant("Roger", "Mateo",485151198,"Primer",)
Estudiant2 = Estudiant("Carlos", "Rodríguez", 478521521, "Segon")
Estudiant3 = Estudiant("Nerea", "Garcia", 457361554, "Cuart")

#Creem professors
Professor1 = Professor("Jorge", "Patriana",485151198,"Programació",)
Professor2 = Professor("Alberto", "Arbeloa", 478521521, "Desenvolupament")
Professor3 = Professor("Marina", "Jimenez", 457361554, "Matematiques")


#Afegir estudiants a l'escola
escola.afegir_estudiants(Estudiant1)
escola.afegir_estudiants(Estudiant2)
escola.afegir_estudiants(Estudiant3)

escola.afegir_professors(Professor1)
escola.afegir_professors(Professor2)
escola.afegir_professors(Professor3)

escola.mostrar_persones()


