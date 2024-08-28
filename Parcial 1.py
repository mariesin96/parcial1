class Estudiante:
    def __init__(self, ID, nombre, edad, promedio_academico, direccion):
        self.ID = ID
        self.nombre = nombre
        self.edad = edad
        self.promedio_academico = promedio_academico
        self.direccion = direccion

class Docente:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def eliminar_ultimo_estudiante(self):
        if len(self.estudiantes) > 0:
            self.estudiantes.pop()

    def procesar_datos(self):
        if len(self.estudiantes) > 0:
            estudiante_mas_alto = max(self.estudiantes, key=lambda x: x.promedio_academico)
            estudiante_mas_joven = min(self.estudiantes, key=lambda x: x.edad)
            promedio_edad = sum([e.edad for e in self.estudiantes]) / len(self.estudiantes)
            return estudiante_mas_alto, estudiante_mas_joven, promedio_edad
        else:
            return None, None, None


docente = Docente()

estudiante1 = Estudiante(1, "Juan", 18, 9.5, "Calle 123")
estudiante2 = Estudiante(2, "Maria", 20, 8.0, "Calle 456")
estudiante3 = Estudiante(3, "Pedro", 22, 7.5, "Calle 789")

docente.agregar_estudiante(estudiante1)
docente.agregar_estudiante(estudiante2)
docente.agregar_estudiante(estudiante3)

estudiante_max, estudiante_joven, promedio_edad = docente.procesar_datos()

print("Estudiante con el promedio academico mas alto:")
print(f"ID: {estudiante_max.ID} - Nombre: {estudiante_max.nombre} - Promedio Academico: {estudiante_max.promedio_academico}")
print()
print("Estudiante mas joven:")
print(f"ID: {estudiante_joven.ID} - Nombre: {estudiante_joven.nombre} - Edad: {estudiante_joven.edad}")
print()
print(f"Promedio de edad de todos los estudiantes: {promedio_edad}") 

