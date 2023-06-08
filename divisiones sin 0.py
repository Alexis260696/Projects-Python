
print("divisions" )
dividend = int(input("write the dividend: "))
divider = int(input("write the divider: "))

if divider == 0:
    print("cannot be divider by 0")
elif dividend % divider == 0:
    print("quotient:" , dividend // divider)
else:
    print("quotient:" , dividend // divider , "Rest:",dividend % divider) 