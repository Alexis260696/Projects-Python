empleados = {}

def menu():
    print("seleccione una opcion\n \n[C]rear empleado\n[B]uscar empleado\n[L]ista de empleados\n[M]odificar empleado\n[E]liminar empleado\n[S]alir")

def obtener_datos(codigo):
    codigoDE =codigo
    nombre = input("\nIngrese el nombre del empleado: ")
    profesion = input("Ingrese la profesion: ")
    return codigoDE, nombre, profesion

def agregar_empleado():
    codigoDE, nombre, profesion = obtener_datos(codigo)
    empleados[codigoDE] = {"nombre": nombre, "profesion": profesion}
    print("\nEmpleado agregado exitosamente")

def buscar_empleado():
    codigo = input("\nIngrese el codigo del empleado: ")
    if codigo.isdigit():
        codigo = int(codigo)
        if codigo in empleados:
            print("\nInformación del empleado")
            print(f"Codigo: {codigo}")
            print(f"Nombre: {empleados[codigo]['nombre']}")
            print(f"Profesión: {empleados[codigo]['profesion']}")
        else:
            print("\nEl empleado ingresado no se encuentra en la base de datos")

def listar_empleados():
    print("\nLista de empleados")
    for empleado in empleados:
        print(f"codigo: {empleado} | Nombre: {empleados[empleado]['nombre']} | Profesión: {empleados[empleado]['profesion']}")

def modificar_empleados():
    codigo = input("\nIngrese el codigo del empleado: ")
    if codigo.isdigit():
        codigo = int(codigo)
        if codigo in empleados:
            print("\nInformación del empleado")
            print(f"Codigo: {codigo}")
            print(f"Nombre: {empleados[codigo]['nombre']}")
            print(f"Profesión: {empleados[codigo]['profesion']}")
            empleados[codigo]['nombre'] = input("Escribe el nuevo nombre del empleado: ")
            empleados[codigo]['profesion'] = input("Escribe la nueva profesion del empleado: ")
        else:
            print("\nEl empleado ingresado no se encuentra en la base de datos")

def eliminar_empleado():
    codigo = input("\nIngrese el codigo del empleado: ")
    if codigo.isdigit():
        codigo = int(codigo)
        if codigo in empleados:
            del empleados[codigo]
            print("\nEmpleado eliminado exitosamente")
        else:
            print("\nEl empleado ingresado no se encuentra en la base de datos")


# variables
codigo = 23123
while True:
    menu()
    opcion = input("\nIngrese una opción: ")

    if opcion == "C" or opcion == "c":
        agregar_empleado()
        codigo += 1

    elif opcion == "B" or opcion == "b":
        buscar_empleado()

    elif opcion == "L" or opcion == "l":
        listar_empleados()

    elif opcion == "M" or opcion == "m":
        modificar_empleados()

    elif opcion == "E" or opcion == "e":
        eliminar_empleado()

    elif opcion == "S" or opcion == "s":
        break

    else:
        print("\nOpción inválida")
