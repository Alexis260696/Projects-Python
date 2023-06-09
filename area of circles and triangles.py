def circle_area_calculator(radius):
	pi = 3.1416
	result = pi * (radius ** 2)
	return result
	
def triangle_area_calculator(base, height):
	result = base * height / 2
	return result
	
while True:
	print("Area Of Circles And Triangles")
	print("Choose A Geometric Figure")
	print("[C]ircle\n[T]riangle\n[E]xit")
	
	answer = input("What Figure Do You Want To Calculate?: ")
	
	if answer == "C" or answer == "c":
		radius = float(input("What Is The Radius Of The Circle?: "))
		print("The Area Of ​​The Circle Is ", circle_area_calculator(radius))
	
	elif answer == "T" or answer == "t":
		triangle_base = int(input ("Enter A Triangle Base: "))
		tringle_height = int(input ("Enter A Triangle Height: ") )
		print("The Area Of The Triangle Is ", triangle_area_calculator(triangle_base, tringle_height))
		
	elif answer == "E" or answer == "e":
		break
		
	else:
		print ("Enter A Valid Command")
        