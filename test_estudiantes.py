from reglas import obtener_estado, calcular_suma
from estudiantes import (
    validar_nota,
    registrar_estudiante,
    estudiantes,
    buscar_estudiante,
)

def test_estado_aprobado():
    assert obtener_estado(24) == "APROBADO"

def test_estado_reprobado():
    assert obtener_estado(18) == "REPROBADO"

def test_estado_reprobado_menor():
    assert obtener_estado(10) == "REPROBADO"

def test_nota_valida():
    assert validar_nota(8)

def test_nota_cero():
    assert validar_nota(0)

def test_nota_diez():
    assert validar_nota(10)

def test_nota_negativa():
    assert not validar_nota(-1)

def test_nota_mayor():
    assert not validar_nota(11)

def test_calcular_suma():
    assert calcular_suma(8, 8, 8) == 24
def test_registrar_estudiante():
    estudiantes.clear()

    registrar_estudiante("Pedro", 8, 8, 8)

    assert len(estudiantes) == 1
    assert estudiantes[0]["nombre"] == "Pedro"
    assert estudiantes[0]["nota1"] == 8
    assert estudiantes[0]["nota2"] == 8
    assert estudiantes[0]["nota3"] == 8
    assert estudiantes[0]["suma"] == 24
    assert estudiantes[0]["estado"] == "APROBADO"

def test_buscar_estudiante_existente():
    estudiantes.clear()

    registrar_estudiante("Ana", 8, 8, 8)

    estudiante = buscar_estudiante("Ana")

    assert estudiante is not None
    assert estudiante["nombre"] == "Ana"

def test_buscar_estudiante_no_existente():
    estudiantes.clear()

    estudiante = buscar_estudiante("No Existe")

    assert estudiante is None