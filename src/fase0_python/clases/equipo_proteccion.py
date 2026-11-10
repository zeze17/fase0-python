class EquipoProteccion:

    def __init__(self, nombre, estado):
        self.nombre = nombre
        self.estado = estado

    def esta_disponible(self):
        return self.estado == "Disponible"
