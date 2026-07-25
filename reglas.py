NOTA_MINIMA_APROBACION = 24

def obtener_estado(suma):
    if suma >= NOTA_MINIMA_APROBACION:
        return "APROBADO"

    return "REPROBADO"