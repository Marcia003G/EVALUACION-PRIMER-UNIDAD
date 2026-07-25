from reglas import obtener_estado

estudiantes = []


def validar_nota(nota):
    return 0 <= nota <= 10


def registrar_estudiante(nombre, nota1, nota2, nota3):
    if nombre == "":
        print("Nombre incorrecto")
        return

    if not validar_nota(nota1):
        print("Nota 1 incorrecta")
        return

    if not validar_nota(nota2):
        print("Nota 2 incorrecta")
        return

    if not validar_nota(nota3):
        print("Nota 3 incorrecta")
        return

    suma = nota1 + nota2 + nota3

    estado = obtener_estado(suma)

    estudiantes.append({
        "nombre": nombre,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "suma": suma,
        "estado": estado
    })

    print("Estudiante registrado")


def listar_estudiantes():
    if len(estudiantes) == 0:
        print("No existen estudiantes")
    else:
        print("LISTA DE ESTUDIANTES")
        for e in estudiantes:
            print(
                e["nombre"],
                e["nota1"],
                e["nota2"],
                e["nota3"],
                e["suma"],
                e["estado"]
            )


def buscar_estudiante(nombre):
    for e in estudiantes:
        if e["nombre"] == nombre:
            return e

    return None

    if not encontrado:
        print("Estudiante no encontrado")