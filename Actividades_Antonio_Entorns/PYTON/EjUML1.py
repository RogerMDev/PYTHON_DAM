
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        print(f"{self.nombre} está HABLANDO!!!!")

    def caminar(self):
        print(f"{self.nombre} con {self.edad} años está CAMINANDO!!!")


class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula

    def estudiar(self):
        print(f"{self.nombre}, con matrícula : {self.matricula} está estudiando!!")


persona1 = Persona("Roger", 25)
persona1.hablar()
estudiante1 = Estudiante("Gerard" , 18, 6969696969)
estudiante1.caminar()
estudiante1.hablar()
estudiante1.estudiar()
