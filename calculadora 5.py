def menu():
    print("[A]ddition\n[S]ubtraction\n[M]ultiplication\n[D]ivision\n[E]xit")

def addition(a, b):
	return a + b
	
def subtraction(a, b):
	return a - b
	
def multiplication(a, b):
	return a * b
	
def division(a, b):
	return a / b
	
def valid_number():
	while True:
		num = input("\nEnter A Number ")
		if not num.isdigit():
			print("\n", error)
		else:
			num = int(num)
			return num
	
#Global Variables
error = "Enter A Valid Number"
	
while True:
	print("\nWelcome To Calculator\n ")
	menu()
	answer = input("\nChoose An Option: ")
	
	if answer == "A" or answer == "a":
		print("\nSum Of Two Numbers")
		a = valid_number()
		b = valid_number()
		print(addition(a, b))
					
	elif answer == "S" or answer == "s":
		print("\nSubstraction Of Two Numbers")
		a = valid_number()
		b = valid_number()
		print("\n", subtraction(a, b))
					
	elif answer == "M" or answer == "m":
		print("\nMultiplication Of Two Numbers")
		a = valid_number()
		b = valid_number()
		print("\n", multiplication(a, b))
					
	elif answer == "D" or answer == "d":
		print("\nDivision Of Two Numbers")
		a = valid_number()
		b = valid_number()
		print("\n", division(a, b))
	
	elif answer == "E" or answer == "e":
		print("\nLeaving, Come Back Soon")
		break
        