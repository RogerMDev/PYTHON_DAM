class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    def set_salario(self, nuevo_salario):
        while nuevo_salario < 0:
            print("Error, el salario no puede ser negativo.")
            nuevo_salario = float(input("Introduce un salario válido (> 0): "))
        self.__salario = nuevo_salario

class Empresa:
    def __init__(self):
        self.lista_empleados = []

    def anadir_empleado(self, empleado):
        self.lista_empleados.append(empleado)

    def mostrar_lista_empleados(self):
        print("Lista de empleados:")
        for indice, empleado in enumerate(self.lista_empleados, start=1):
            print(f"{indice}. {empleado.nombre}, {empleado.edad} años, {empleado.get_salario()} €")

print("EJERCICIO 1")
empresa1 = Empresa()
empresa1.anadir_empleado(Empleado("Roger", 25, 3000))
empresa1.anadir_empleado(Empleado("Carlos", 50, 2000))
empresa1.anadir_empleado(Empleado("Marina", 30, 7000))
empresa1.anadir_empleado(Empleado("Eric", 27, 2400))
empresa1.mostrar_lista_empleados()
print("---------------------")

print("EJERCICIO 2")
empleado1 = Empleado("Francisco", 53, 1500)
empleado1.set_salario(2000)
print(f"Salario actualizado: {empleado1.get_salario()} €")
print("---------------------")

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento

    def mostrar_informacion(self):
        print(f"El gerente {self.nombre}, de {self.edad} años, trabaja en el departamento {self.departamento}.")

print("EJERCICIO 3")
gerente1 = Gerente("Roger", 55, 1500, "IT")
gerente1.mostrar_informacion()
print("---------------------")

# Trabaja con listas y diccionarios para gestionar múltiples objetos.
# Requisitos:
# 1. Crea una lista de objetos 'Empleado' y ordena la lista por salario.
# 2. Usa un diccionario para almacenar empleados por su ID y recuperarlos rápidamente.

print("EJERCICIO 5")

# Lista de empleados
empleados = [
    Empleado("Carlos", 25, 2500),
    Empleado("Ana", 33, 3200),
    Empleado("Beatriz", 31, 2800),
]

# Ordenar la lista por salario
empleados.sort(key=lambda e: e.get_salario())

# Mostrar los empleados ordenados
print("Lista de empleados ordenados por salario:")
for empleado in empleados:
    print(f"{empleado.nombre}, {empleado.edad} años, {empleado.get_salario()} €")
print("---------------------")
