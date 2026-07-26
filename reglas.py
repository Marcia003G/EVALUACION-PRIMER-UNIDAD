NOTA_MINIMA_APROBACION = 24
NOTA_MINIMA_ASIGNATURA = 5

def obtener_estado(suma, nota1, nota2, nota3):
    if (
        suma >= NOTA_MINIMA_APROBACION
        and nota1 >= NOTA_MINIMA_ASIGNATURA
        and nota2 >= NOTA_MINIMA_ASIGNATURA
        and nota3 >= NOTA_MINIMA_ASIGNATURA
    ):
        return "APROBADO"

    return "REPROBADO"

def calcular_suma(nota1, nota2, nota3):
    return nota1 + nota2 + nota3