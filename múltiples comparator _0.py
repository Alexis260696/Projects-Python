print("multiples comparator")
a = int(input("write a number: "))
b = int(input("write oter number: "))

if a < 0 or b < 0:
    print("sorry, you cant write negative numbers")
elif a >= b and a % b != 0:
    print(a , "is not a multiple of ", b)
elif a >= b and a % b == 0:
    print(a , "is a multiple of " , b)
elif a < b and b % a != 0:
    print(b , " is not a multiple of " , a)
else:
    print(b , "is a multiple of " , a)