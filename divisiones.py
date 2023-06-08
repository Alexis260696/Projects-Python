print("divisions" )
dividend = int(input("write the dividend: "))
divider = int(input("write the divider: "))

if dividend % divider == 0:
    print(" quotient: " , dividend // divider)
else:
    print(" quotient: " , dividend // divider , "Rest: ",dividend % divider)