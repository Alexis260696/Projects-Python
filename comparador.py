print("number comparator")
number1 = float(input("write a number: "))
number2 = float(input("write oter number: "))

if number1 > number2:
    print("minor:", number2, "major:", number1)
elif number1 < number2:
    print("minor:", number1, "major:", number2)
else:
    print("both number are the same")