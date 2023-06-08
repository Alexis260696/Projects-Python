print("equation: a x + b = 0")
a=float(input("enter a number a "))
b=float(input("enter a number b "))

if a == b and b == 0:
    print("all numbers are solution")
elif a == 0:
    print("this equation has not solution")
else:
    print("this equation has a solution")