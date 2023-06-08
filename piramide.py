bandera = 1
while bandera:
    
    print("piramide")
    print("elige hacia donde quieres que apunte la piramide")
    print("1.- arriba ")
    print("2.- abajo ")
    print("3.- izquierda ")
    print("4.- derecha ")
    r = input("elige una opcion ")
    b = 0
    
    if r == "1" or r == "2" or r == "3" or r == "4":
        print("bien ")
        
        if r == "1":
            print("elige un numero ")
            b = input("escribe un numero ")

            if b.isdigit():
                b = int(b)
                if b % 2 != 0:
                    for i in range(0, b + 1):
                        e = b-1
                        if i % 2 != 0 and e >= 0:
                            print(" " * e, "*" * i)
                            b -= 1
                            e += 2

                elif b % 2 == 0:
                    for i in range(0, b + 1):
                        e = b - 1
                        if i % 2 == 0 and e >= 0:
                            print(" " * e, "*" * i)
                            b -= 1
                            e += 2

            else:
                print("error al escribir base ")


        elif r == "2":
            print("elige un numero ")
            b = input("escribe un numero ")

            if b.isdigit():
                b = int(b)
                if b % 2 != 0:
                    for i in range(0, b + 1):
                        e = b - 1
                        if i % 2 != 0 and e >= 0:
                            print(" " * e, "*" * i)
                            b -= 1
                            e += 2

                elif b % 2 == 0:
                    for i in range(0, b + 1):
                        e = b - 1
                        if i % 2 == 0 and e >= 0:
                            print(" " * e, "*" * i)
                            b -= 1
                            e += 2
                        


                
    else:
        print(" error ")
    