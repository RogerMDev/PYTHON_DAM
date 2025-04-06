#Començem a fer Crea un diagrama de classes per a un sistema que gestioni projectes de desenvolupament de programari.
#CREEM LA CLASSE PARE
class Projecte:
    def __init__ (self, nom, durada, llenguatge_principal):
        self.nom = nom
        self.durada = durada
        self.llenguatge_principal = llenguatge_principal
        self.tasques = []

#CREEM CLASSE PROJECTE INTERN, SUBCLASSE DE PROJECTE
class ProjecteIntern(Projecte):
    def __init__ ( self, nom, durada, llenguatge_principal, responsable, departament):
        super().__init__(nom, durada,llenguatge_principal)
        self.responsable = responsable
        self.departament = departament

#AFEGIM ELS MÈTODES PROPIS A LA CLASSE PROJECTE INTERN
    def mostrar_informacio(self):
        print(f" Nom: {self.nom}, Durada: {self.durada}, Llenguatge Principal: {self.llenguatge_principal}, Responsable: {self.responsable}, Departament: {self.departament}")

    def afegir_tasca(self,tasca):
        self.tasques.append(tasca)

#CREEM CLASSE PROJECTE EXTERN, SUBCLASSE DE PROJECTE
class ProjecteExtern(Projecte):
    def __init__ (self, nom, durada,  llenguatge_principal, client, pressupost):
        super().__init__(nom, durada, llenguatge_principal)
        self.client = client
        self.pressupost = pressupost

# AFEGIM ELS MÈTODES PROPIS A LA CLASSE PROJECTE EXTERN
    def mostrar_informacio(self):
        print(f"Projecte: {self.nom}, Duracio: {self.durada}, Llenguatge: {self.llenguatge_principal}, Client: {self.client}, Pressupost: {self.pressupost}")

# CREEM LA CLASSE EQUIP
class Equip:
    def __init__ (self, nom_equip):
        self.nom_equip = nom_equip
        self.membres = []

#AFEGIM ELS MÈTODES PROPIS DE LA CLASSE EQUIP
    def afegir_membre(self, membre):
        self.membres.append(membre)

    def mostrar_informacio(self):
        print(f"Equip: {self.nom_equip}, Membres: {self.membres}")

# CREEM LA CLASSE MEMBRE
class Membre:
    def __init__(self, nom, rol, experiencia):
        self.nom = nom
        self.rol = rol
        self.experiencia = experiencia

# AFEGIM ELS MÈTODES PROPIS DE LA CLASSE MEMBRE
    def mostrar_membres(self):
        print(f" Membre: {self.nom}, Rol: {self.experiencia}, Experiència: {self.experiencia}")

#CREEM LA CLASSE TASQUES
class Tasques:
    def __init__(self, titol, estat, responsable):
        self.titol= titol
        self.estat = estat
        self.responsable = responsable

# AFEGIM ELS MÈTODES PROPIS DE LA CLASSE TASQUES
    def mostrar_tasques(self):
        print(f"Tasca: {self.titol}, Estat: {self.estat}, Responsable: {self.responsable}")

if __name__ == "__main__":
    # Crear un projecte intern
    projecte_intern = ProjecteIntern(
        nom="Aplicació CRM Interna",
        durada=12,
        llenguatge_principal="Python",
        responsable="Joan Rovira",
        departament="IT"
    )
    # Crear un projecte extern
    projecte_extern = ProjecteExtern(
        nom="Plataforma E-learning",
        durada=18,
        llenguatge_principal="Java",
        client="Educorp",
        pressupost="300k"
    )
    # Crear un equip i membres
    equip = Equip("Equip Desenvolupament")
    membre1 = Membre("Anna", "Desenvolupadora", 3)
    membre2 = Membre("Marc", "Tester", 2)
    equip.afegir_membre(membre1)
    equip.afegir_membre(membre2)

    # Afegir tasques al projecte intern
    tasca1 = Tasques("Definir requeriments", "pendent", membre1)
    tasca2 = Tasques("Provar funcionalitats", "pendent", membre2)
    projecte_intern.afegir_tasca(tasca1)
    projecte_intern.afegir_tasca(tasca2)

    # Mostrar informació del projecte intern
    print("Informació del projecte intern:")
    print(projecte_intern.mostrar_informacio())
    print("\nTasques del projecte intern:")
    print(tasca1.mostrar_tasques())
    print(tasca2.mostrar_tasques())

    # Mostrar informació de l'equip
    print("\nInformació de l'equip:")
    print(equip.mostrar_informacio())
    print("\nMembres de l'equip:")
    print(membre1.mostrar_membres())
    print(membre2.mostrar_membres())

    # Mostrar informació del projecte extern
    print("\nInformació del projecte extern:")
    print(projecte_extern.mostrar_informacio())