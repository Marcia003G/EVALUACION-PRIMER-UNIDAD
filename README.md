Sistema de Registro de Estudiantes

# Descripción del sistema

Este proyecto es un sistema que permite el registro y consulta de estudiantes y sus calificaciones.

En el sistema se puede registrar un estudiante con tres notas, validar que las calificaciones se encuentren dentro del rango permitido, calcular la suma de las notas, determinar el estado académico y buscar estudiantes registrados.

# Objetivo de la actividad

El objetivo de la actividad es aplicar técnicas de Código Limpio, refactorización, separación de responsabilidades, diseño orientado al cambio, pruebas automatizadas y control de versiones mediante Git y GitHub.

El proyecto inició a partir de un código funcional, el cual, a través de varios cambios registrados mediante commits independientes, el sistema fue mejorado progresivamente.

# Funcionamiento general

El sistema permite realizar las siguientes operaciones:

- Registrar estudiantes.
- Validar las calificaciones.
- Calcular la suma de tres notas.
- Determinar el estado académico.
- Listar los estudiantes registrados.
- Buscar estudiantes por nombre.

# Reglas académicas actuales

Para que un estudiante sea APROBADO, debe cumplir simultáneamente con las siguientes condiciones:

* La suma de las tres notas debe ser mayor o igual a 24 puntos.
* Cada nota individual debe ser mayor o igual a 5 puntos.

Por ejemplo:
8 + 8 + 8 = 24 → APROBADO

En cambio:
10 + 10 + 4 = 24 → REPROBADO

Aunque la suma alcanza 24 puntos, una de las notas individuales es menor que 5.

# Estructura del proyecto

```text
Evaluacion_primera_unidad/
│
├── estudiantes.py
├── reglas.py
├── main.py
├── test_estudiantes.py
├── README.md
└── .gitignore
```

#     estudiantes.py

Contiene la lógica relacionada con la gestión de estudiantes:

* validación de notas;
* registro de estudiantes;
* listado de estudiantes;
* búsqueda de estudiantes.

#     reglas.py

Contiene las reglas académicas del sistema:

* cálculo de la suma de las calificaciones;
* determinación del estado académico;
* constantes relacionadas con las condiciones de aprobación.

La separación de estas reglas permite modificar los criterios académicos con un impacto reducido sobre el resto del sistema.

#     main.py

Contiene la ejecución principal del programa y utiliza las funciones disponibles en el módulo de estudiantes.

#     test_estudiantes.py

Contiene las pruebas automatizadas desarrolladas utilizando Pytest.

#      .gitignore

Evita que archivos generados automáticamente por Python y Pytest sean incluidos en el repositorio, como:

- `__pycache__/`;
- archivos `.pyc`;
- `.pytest_cache/`.

# Mejoras realizadas

Durante la evolución del sistema se realizaron las siguientes mejoras:

1. Se incorporó el código inicial al repositorio.
2. Se mejoraron los nombres de funciones y variables para aumentar la legibilidad.
3. Se creó una función reutilizable para validar las calificaciones.
4. Se separaron las reglas académicas de la lógica de gestión de estudiantes.
5. Se organizaron las responsabilidades en módulos independientes.
6. Se creó una función específica para calcular la suma de las calificaciones.
7. Se implementaron pruebas automatizadas utilizando Pytest.
8. Se agregaron pruebas para la validación de notas.
9. Se agregaron pruebas para el cálculo de la suma.
10. Se agregaron pruebas para el registro de estudiantes.
11. Se agregaron pruebas para la búsqueda de estudiantes.
12. Se incorporó una nueva regla académica relacionada con la nota mínima individual por asignatura.
13. Se utilizó Git y GitHub para registrar progresivamente la evolución del sistema.

# Pruebas automatizadas

Las pruebas fueron implementadas utilizando `pytest`.

Para ejecutar todas las pruebas, utilizar:

```bash
py -m pytest
```

Las pruebas verifican:

* notas válidas;
* notas fuera del rango permitido;
* cálculo de la suma de calificaciones;
* determinación del estado académico;
* registro de estudiantes;
* búsqueda de estudiantes existentes;
* búsqueda de estudiantes inexistentes;
* aplicación de la regla de nota mínima por asignatura.

# Ejecución del programa

Para ejecutar el programa principal:

```bash
py main.py
```

# Control de versiones

Los cambios significativos se registraron mediante commits independientes y descriptivos. Esto permite observar la evolución del sistema desde el código inicial hasta una versión con:

* mejor organización;
* responsabilidades separadas;
* reglas académicas independientes;
* pruebas automatizadas;
* documentación del proyecto.

# Tecnologías utilizadas

* Python 3
* Pytest
* Git
* GitHub