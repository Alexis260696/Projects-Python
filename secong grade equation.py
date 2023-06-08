while(True):
    print("a x**2 + b x + c = 0")
    a = float(input("enter a number a "))
    b = float(input("enter a number b "))
    c = float(input("enter a number c "))
    d = b**2 - 4 * a * c
    if a == b and b == c and c == 0:
        print("all numbers are solution")
    elif a == b and b == 0:
        print("this equation has not a solution")
    elif a == 0:
        print("this equation has a solution", - c / b)
    elif d < 0:
        print("this equation has not a real solution")
    elif d == 0:
        print("this equation has a solution" , -b / (2*a))
    else:
        print("this equation has a two solutions" , (- b - d ** 0.5)/(2 * a) , "o " , (- b + d ** 0.5)/(2 * a))