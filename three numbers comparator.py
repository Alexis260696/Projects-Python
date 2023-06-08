print("three numbers comparator")
a = float(input("write a number: "))
b = float(input("write oter number: "))
c = float(input("write oter number: "))

if a != b and a != c and b != c:
    print("they are diferent numbers")
elif a == b == c:
    print("all three numbers are the same")
else:
    print("two numbers are equal")