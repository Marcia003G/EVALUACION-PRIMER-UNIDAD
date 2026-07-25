from reglas import obtener_estado, calcular_suma
from estudiantes import validar_nota

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