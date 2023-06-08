a = 1
while a == 1:

    print("factorial")
    n = input("escribe un numero ")

    if not n.isdigit():
        print("error")
    else:
        n = int(n)
        for i in range(1, n):
            n *= i

        print("el factorial es ", n)
