a = 0
b = 1
bandera = 1
while bandera:
    print(" fibonacci ")
    n = input("write a number ")

    if not n.isdigit():
        print("error")
    else:
        n = int(n)
        for i in range(0,n):
            if i <= 1:
                print(i)
            else:
                c = a + b
                a = b
                b = c
                print(c)


