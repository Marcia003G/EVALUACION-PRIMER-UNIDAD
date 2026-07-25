estudiantes = []

def registrar_estudiante(nombre, nota1, nota2, nota3):
    if nombre == "":
        print("Nombre incorrecto")
        return

    if nota1 < 0 or nota1 > 10:
        print("Nota incorrecta")
        return

    if nota2 < 0 or nota2 > 10:
        print("Nota incorrecta")
        return

    if nota3 < 0 or nota3 > 10:
        print("Nota incorrecta")
        return

    suma = nota1 + nota2 + nota3

    if suma >= 24:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

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
    encontrado = False

    for e in estudiantes:
        if e["nombre"] == nombre:
            print(
                e["nombre"],
                e["nota1"],
                e["nota2"],
                e["nota3"],
                e["suma"],
                e["estado"]
            )
            encontrado = True

    if encontrado == False:
        print("Estudiante no encontrado")


registrar_estudiante("Ana", 8, 8, 8)
registrar_estudiante("Luis", 6, 6, 6)
registrar_estudiante("Carlos", 10, 9, 8)

listar_estudiantes()

buscar_estudiante("Ana")