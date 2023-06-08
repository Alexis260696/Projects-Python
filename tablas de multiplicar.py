a = 1
while a == 1:

    print("tablas de multiplicar")
    x = input("ingresa un numero ")

    if not x.isdigit():
        print("error")
    else:
        x = int(x)
        for i in range(1,11):
            print(x, " * ", i, " = ", x * i)
        a = 0
