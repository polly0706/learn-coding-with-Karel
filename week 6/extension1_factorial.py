"""
File: extension1_factorial.py
Name: Polly
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

EXIT = -100

def main():
	print("Welcome to stanCode factorial master!")
	enter = int(input("Give me a number, and I will list the answer of factorial:"))


	while enter != EXIT:
		a = enter
		while a !=1:
			enter = enter * (a-1)
			a -= 1
		print("Answer:", enter)
		enter = int(input("Give me a number, and I will list the answer of factorial:"))

	print("- - - - - - See ya!-------------")

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()