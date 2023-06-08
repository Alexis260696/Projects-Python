print ("cm converter")
cm = int(input("write a quantity in centimeters "))
km = cm // 100000
m = cm % 100000 // 100
rest = cm % 100

if km == 0:
    print (cm,"cm" "= ",m,"m,",rest,"cm.")
elif m == 0:
    print (cm,"cm" "= ",km,"km,",rest,"cm.")
elif rest == 0:
    print (cm,"cm" "= ",km,"km,",m,"m,")
else:
    print (cm,"cm" "= ",km,"km,",m,"m,",rest,"cm.")