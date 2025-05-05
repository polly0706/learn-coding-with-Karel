"""
File: my_power_function.py
Name: 
-------------------------------
This program shows students how to 
make their own functions by defining
def my_power(a, b)
"""

def addition(n1,n2):
	result = n1+n2
	return result

def subtract(n1,n2):
	return n2-n1

def power(n1,n2):
	a = 1
	for i in range(n2):
		a = a*n1
	return a


def main():
	a = int(input("a:"))
	b = int(input("b:"))

	answer = addition(a,b)
	print(answer)

	answer= subtract(a,b)
	print(answer)

	answer = power(a,b)
	print(answer)



	"""
	print('This program prints a to the power of b.')
	a = int(input('a: '))
	b = int(input('b: '))
	print(my_power(a, b))
	"""

def my_power(a, b):
	pass


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
