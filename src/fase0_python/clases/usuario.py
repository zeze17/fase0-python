from dataclasses import dataclass

@dataclass
class Usuario:
    nombre: str
    edad: int
    cargo: str

    def es_mayor_de_edad(self):
        return self.edad >= 18
