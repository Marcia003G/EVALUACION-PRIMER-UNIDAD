NOTA_MINIMA_APROBACION = 24

def obtener_estado(suma):
    if suma >= NOTA_MINIMA_APROBACION:
        return "APROBADO"

    return "REPROBADO"
    
def calcular_suma(nota1, nota2, nota3):
    return nota1 + nota2 + nota3