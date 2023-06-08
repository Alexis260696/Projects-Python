bandera = 1
while bandera:
    
    print("calculadora ")
    print("selecciona una opcion ")
    print("1.- sumar  ")
    print("2.- restar ")
    print("3.- dividir  ")
    print("4.- multiplicar ")
    print("5.- salir ")
    r = input("elige una opcion ")
    
    if r == "1" or r == "2" or r == "3" or r == "4" or r == "5":
        print("bien ") 
               
        if r == "1":
            print(" suma ")
            print(" elije los numeros a sumar")
            a = input(" escribe el numero a ")
            if a.isdigit():
                a = int(a)
                b = input(" escribe el numero b ")
                if b.isdigit():
                    b = int(b)
                    c = a + b 
                    print(c) 
                else:
                    print(" error ")
            else:
                print(" error ") 
                
        elif r == "2":
            print(" resta ")
            print(" elige los nuneros a restar")
            a = input(" escribe el numero a ")
            if a.isdigit():
                a = int(a)
                b = input(" escribe el numero b ")
                if b.isdigit():
                    b = int(b)
                    c = a - b
                    print(c) 
                else:
                    print(" error ")
            else:
                print(" error ")
                
        elif r == "3":
            print(" division ")
            print(" elige los nuneros a dividir ")
            a = input(" escribe el numero a ")
            if a.isdigit():
                a = int(a)
                b = input(" escribe el numero b ")
                if b.isdigit():
                    b = int(b)
                    c = a / b
                    print(c) 
                else:
                    print(" error ")
            else:
                print(" error ")
                
        elif r == "4":
            print(" multiplicacion ")
            print(" elige los nuneros a multiplicar ")
            a = input(" escribe el numero a ")
            if a.isdigit():
                a = int(a)
                b = input(" escribe el numero b ")
                if b.isdigit():
                    b = int(b)
                    c = a * b
                    print(c) 
                else:
                    print(" error ")
            else:
                print(" error ")
                             
        elif r == "5":
            print(" adios ")
            bandera = 0
                                  
    else:
        print(" error ")
