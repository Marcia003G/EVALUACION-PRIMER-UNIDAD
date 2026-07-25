from estudiantes import (
    registrar_estudiante,
    listar_estudiantes,
    buscar_estudiante,
)

registrar_estudiante("Ana", 8, 8, 8)
registrar_estudiante("Luis", 6, 6, 6)
registrar_estudiante("Carlos", 10, 9, 8)

listar_estudiantes()

estudiante = buscar_estudiante("Ana")

if estudiante:
    print(estudiante)
else:
    print("Estudiante no encontrado")