print("date comparator")
date1 = int(input("write a year: "))
date2 = int(input("write a year: "))

if date1 > date2:
    print("past ", date1 - date2 ," years")
elif date1 < date2:
    print(date2 - date1, "years to go")
else:
    print("they are the same year")