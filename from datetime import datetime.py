from datetime import datetime

class Paciente:
    def __init__(self, ci, nombre, telefono):
        self.ci = ci
        self.nombre = nombre
        self.telefono = telefono


class Medico:
    def __init__(self, codigo, nombre, especialidad):
        self.codigo = codigo
        self.nombre = nombre
        self.especialidad = especialidad


class CitaMedica:
    def __init__(self, paciente, medico, fecha, hora):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.hora = hora
        self.estado = "Programada"

    def mostrar_cita(self):
        print("\n--- CITA MÉDICA ---")
        print(f"Paciente: {self.paciente.nombre}")
        print(f"CI: {self.paciente.ci}")
        print(f"Médico: {self.medico.nombre}")
        print(f"Especialidad: {self.medico.especialidad}")
        print(f"Fecha: {self.fecha}")
        print(f"Hora: {self.hora}")
        print(f"Estado: {self.estado}")


class SistemaCitas:
    def __init__(self):
        self.pacientes = []
        self.medicos = []
        self.citas = []

    def registrar_paciente(self):
        ci = input("Ingrese CI del paciente: ")
        nombre = input("Ingrese nombre del paciente: ")
        telefono = input("Ingrese teléfono del paciente: ")

        paciente = Paciente(ci, nombre, telefono)
        self.pacientes.append(paciente)
        print("Paciente registrado correctamente.")

    def registrar_medico(self):
        codigo = input("Ingrese código del médico: ")
        nombre = input("Ingrese nombre del médico: ")
        especialidad = input("Ingrese especialidad: ")

        medico = Medico(codigo, nombre, especialidad)
        self.medicos.append(medico)
        print("Médico registrado correctamente.")

    def buscar_paciente(self, ci):
        for paciente in self.pacientes:
            if paciente.ci == ci:
                return paciente
        return None

    def buscar_medico(self, codigo):
        for medico in self.medicos:
            if medico.codigo == codigo:
                return medico
        return None

    def programar_cita(self):
        ci = input("Ingrese CI del paciente: ")
        paciente = self.buscar_paciente(ci)

        if paciente is None:
            print("Paciente no encontrado.")
            return

        codigo = input("Ingrese código del médico: ")
        medico = self.buscar_medico(codigo)

        if medico is None:
            print("Médico no encontrado.")
            return

        fecha = input("Ingrese fecha de la cita (dd/mm/aaaa): ")
        hora = input("Ingrese hora de la cita (hh:mm): ")

        for cita in self.citas:
            if cita.medico.codigo == codigo and cita.fecha == fecha and cita.hora == hora:
                print("Error: El médico ya tiene una cita en ese horario.")
                return

        nueva_cita = CitaMedica(paciente, medico, fecha, hora)
        self.citas.append(nueva_cita)
        print("Cita médica programada correctamente.")

    def mostrar_citas(self):
        if len(self.citas) == 0:
            print("No existen citas registradas.")
        else:
            for cita in self.citas:
                cita.mostrar_cita()

    def cancelar_cita(self):
        ci = input("Ingrese CI del paciente: ")
        fecha = input("Ingrese fecha de la cita a cancelar: ")

        for cita in self.citas:
            if cita.paciente.ci == ci and cita.fecha == fecha:
                cita.estado = "Cancelada"
                print("Cita cancelada correctamente.")
                return

        print("No se encontró la cita.")


def menu():
    sistema = SistemaCitas()

    while True:
        print("\n===== SISTEMA DE CITAS MÉDICAS =====")
        print("1. Registrar paciente")
        print("2. Registrar médico")
        print("3. Programar cita médica")
        print("4. Mostrar citas")
        print("5. Cancelar cita")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema.registrar_paciente()
        elif opcion == "2":
            sistema.registrar_medico()
        elif opcion == "3":
            sistema.programar_cita()
        elif opcion == "4":
            sistema.mostrar_citas()
        elif opcion == "5":
            sistema.cancelar_cita()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")


menu()


