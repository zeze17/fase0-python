from fase0_python.clases.departamento import Departamento

def test_departamento():
    departamento1 = Departamento("Sistemas", "DEP001", "Carlos", True, 15)

    departamento1.mostrar_informacion()
    assert departamento1.equipo_disponible() == "Sistemas equipo disponible"
    assert departamento1.agregar_persona() == 16

    departamento1.mostrar_informacion()

def test_departamento_false():
    dept = Departamento("Sistemas", "DEP001", "Carlos", False, 0)

    dept.mostrar_informacion()
    assert dept.equipo_disponible() == "Sistemas no equipo disponible"
    assert dept.agregar_persona() == 1
    assert dept.eliminar_persona() == 0
    assert dept.eliminar_persona() == 0
    assert dept.cambiar_disponibilidad() == True

    dept.mostrar_informacion()