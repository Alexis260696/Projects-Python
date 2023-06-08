bandera = 1
while bandera:

    print(" calcula el promedio del salon ")
    print(" escribe la calificacion de al menos 10 alumnos para calcular el promedio general del salon ")

    alumnos = input("escribe la cantidad de alumnos ")
    if alumnos.isdigit():
        alumnos = int(alumnos)
        if alumnos >= 10:
            total = 0

            for i in range(1, alumnos + 1):
                x = 1

                    print("escribe la calificacion del alumno  ", i)
                while x:
                    calificaciones = input()
                    if calificaciones.isdigit():
                        calificaciones = int(calificaciones)
                        total += calificaciones
                        x = 0
                    else:
                        print("error ")
            print("promedio general ", total / alumnos)

        else:
            print("escribe un numero mayor o igual a diez ")

    else:
        print("escribe un numero")
