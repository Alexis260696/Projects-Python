print("leap year comparator")
date = int(input("write a year:"))

if date % 400 == 0 or date % 100 != 0 and date % 4 == 0:
    print( date , "is a leap year")
else:
    print(date , "is not a leap year")