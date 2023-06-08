print("areas of circles and triangles")
print("choose a geometric figure")
print("C = circle", "T = triangle ")
R = input("What figure do you want to calculate?")
if R == "C"or R == "c":
    r = float(input("what is the radius of the circle?"))
    pi = 3.1416
    print(pi * r**2)
elif R == "T" or R == "t":
    ca = int(input ("enter a number ca ") )
    co = int(input ("enter a number co ") )
    h2 = ca*ca + co*co 
    h = h2 ** 0.5
    print (h)
else:
    print ("chinga tu madre te pedi C o T no tus mamadas ")