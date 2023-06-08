bandera = 1
while bandera:

    print(" calcula el promedio del salon ")
    print(" escribe la calificacion de 10 alumnos para calcular el promedio general del salon ")

    a = input(" escribe la calificacion 1 ")
    if a.isdigit():
        a = int(a)
        b = input(" escribe la calificacion 2 ")
        if b.isdigit():
            b = int(b)
            c = input(" escribe la calificacion 3 ")
            if c.isdigit():
                c = int(c)
                d = input(" escribe la calificacion 4 ")
                if d.isdigit():
                    d = int(d)
                    e = input(" escribe la calificacion 5 ")
                    if e.isdigit():
                        e = int(e)
                        f = input(" escribe la calificacion 6 ")
                        if f.isdigit():
                            f = int(f)
                            g = input(" escribe la calificacion 7 ")
                            if g.isdigit():
                                g = int(g)
                                h = input(" escribe la calificacion 8 ")
                                if h.isdigit():
                                    h = int(h)
                                    i = input(" escribe la calificacion 9 ")
                                    if i.isdigit():
                                        i = int(i)
                                        j = input(" escrie la calificacion 10 ")
                                        if j.isdigit():
                                            j = int(j)

                                            pro = a+b+c+d+e+f+g+h+i+j
                                            print(" promedio general ")
                                            print(pro / 10)

                                        else:
                                            print(" error ")
                                    else:
                                        print(" error ")
                                else:
                                    print(" error ")
                            else:
                                print(" error ")
                        else:
                            print(" error ")
                    else:
                        print(" error ")
                else:
                    print(" error ")
            else:
                print(" error ")
        else:
            print(" error ")
    else:
        print(" error ")
