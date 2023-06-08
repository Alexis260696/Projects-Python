print("date comparator")
date1 = int(input("write a year: "))
date2 = int(input("write a year: "))

if date1 > date2:  
    if date1 - date2 == 1:
        print("it's been 1 year")
    else:    
        print("past " , date1 - date2 , "years")
        
elif date1 < date2:
    if date1 - date2 == -1:
        print("1 year to go")
    else:
        print(date2 - date1, "years to go")
else:
    print("they are the same year")