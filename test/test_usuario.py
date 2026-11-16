from fase0_python.clases.usuario import Usuario
from fase0_python.clases.equipo_proteccion import EquipoProteccion


def test_obtener_nombre():
    usuario = Usuario("Carlos", 25, "Operario")

    assert usuario.nombre == "Carlos"


def test_usuario_mayor_edad():
    usuario = Usuario("Carlos", 25, "Operario")

    assert usuario.es_mayor_de_edad() == True


def test_usuario_menor_edad():
    usuario = Usuario("Andres", 16, "Aprendiz")

    assert usuario.es_mayor_de_edad() == False


def test_equipo_disponible():
    casco = EquipoProteccion("Casco", True)

    assert casco.estado == True


def test_equipo_no_disponible():
    guantes = EquipoProteccion("Guantes", False)

    assert guantes.estado == False
