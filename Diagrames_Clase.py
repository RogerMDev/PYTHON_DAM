#Començem a fer Crea un diagrama de classes per a un sistema que gestioni projectes de desenvolupament de programari.
class Projecte:
    def __init__ (self, nom, durada, llenguatge_principal):
        self.nom = nom
        self.durada = durada
        self.llenguatge_principal = llenguatge_principal
        self.responsable = responsable
        self.departament = departament

        def get_nom(self):
            print(f"El nom és")
class ProjecteExtern(Projecte):
    super().__init__(nom, durada,llenguatge_principal)
    def __init__ (self, client, pressupost):
        self.client = client
        self.pressupost = pressupost

class Equip:
    def __init__ (self, nom_equip, membres):
        self.nom_equip = nom_equip
        self.membres = membres

class Membre(Equip):
    def __init__(self, nom, rol, experiencia):
        self.nom = nom
        self.rol = rol
        self.experiencia = experiencia

class Tasques:
    def __init__(self, titol, estat, responsable):
        self.titol= titol
        self.estat = estat
        self.responsable = responsable

if __name__ == "__main__":
    # Crear un projecte intern
    projecte_intern = ProjecteIntern(
        nom="Aplicació CRM Interna",
        duracio=12,
        llenguatge="Python",
        responsable="Joan Rovira",
        departament="IT"
    )
    # Crear un projecte extern
    projecte_extern = ProjecteExtern(
        nom="Plataforma E-learning",
        duracio=18,
        llenguatge="Java",
        client="Educorp",
        pressupost=300
    )
    # Crear un equip i membres
    equip = Equip("Equip Desenvolupament")
    membre1 = Membre("Anna", "Desenvolupadora", 3)
    membre2 = Membre("Marc", "Tester", 2)
    equip.afegir_membre(membre1)
    equip.afegir_membre(membre2)
    # Afegir tasques al projecte intern
    tasca1 = Tasca("Definir requeriments", "pendent", membre1)
    tasca2 = Tasca("Provar funcionalitats", "pendent", membre2)
    projecte_intern.afegir_tasca(tasca1)
    projecte_intern.afegir_tasca(tasca2)
    # Mostrar informació del projecte intern
    print("Informació del projecte intern:")
    print(projecte_intern.mostrar_informacio())
    print("\nTasques del projecte intern:")
    print(projecte_intern.mostrar_tasques())
    # Mostrar informació de l'equip
    print("\nInformació de l'equip:")
    print(equip.mostrar_informacio())
    print("\nMembres de l'equip:")
    print(equip.mostrar_membres())
    # Mostrar informació del projecte extern
    print("\nInformació del projecte extern:")
    print(projecte_extern.mostrar_informacio())