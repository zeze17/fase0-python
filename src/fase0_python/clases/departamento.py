from dataclasses import dataclass

@dataclass
class Departamento:

    nombre: str
    identificador: str
    lider: str
    disponible: bool
    numero_personas: int

    def cambiar_disponibilidad(self):
        self.disponible = not self.disponible
        return self.disponible

    def agregar_persona(self):
        self.numero_personas += 1
        return self.numero_personas

    def eliminar_persona(self):
        if self.numero_personas > 0:
            self.numero_personas -= 1
            return  self.numero_personas

        return 0

    def equipo_disponible(self):
        if self.numero_personas >= 5:
            return self.nombre + " equipo disponible"
        else:
            return self.nombre + " no equipo disponible"

    def mostrar_informacion(self):
        print(f"Departamento: {self.nombre}")
        print(f"Identificador: {self.identificador}")
        print(f"Líder: {self.lider}")
        print(f"Disponible: {self.disponible}")
        print(f"Número de personas: {self.numero_personas}")