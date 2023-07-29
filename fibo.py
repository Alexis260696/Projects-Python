def fibo(n):
	if n <= 1:
		return n
	else:
		return fibo(n-1) + fibo(n-2)

while True:		
	number = input('Please enter a number ')
	if not number.isdigit():
		print('Enter a valid number')
	else:
		number = int(number)
		print('The number ', number, 'in the fibonacci secuence is :', fibo(number -1))
		for i in range(number):
			print(fibo(i))
