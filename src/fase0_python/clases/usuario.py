class Usuario:

    def __init__(self, nombre, edad, cargo):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo

    def obtener_nombre(self):
        return self.nombre

    def es_mayor_de_edad(self):
        return self.edad >= 18
