"""
File: prime_checker.py
Name:
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100

def main():
	print("Welcome to the prime checker!")
	number = int(input("n:"))


	while number != EXIT:
		icon = 0
		a = 2
		while a < number:
			if number % a == 0:
				print(number, "is not a prime number.")
				icon = 1
				break
			else:
				a += 1
#		print (icon)
		if icon != 1:
			print(number, "is a prime number.")
		number = int(input("n:"))

	print("Have a good one!")

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
