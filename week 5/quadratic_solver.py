"""
File: quadratic_solver.py
Name:Polly
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	print("stanCode Quadratic Solver!")

	a = int(input("Enter a = "))
	b = int(input("Enter b = "))
	c = int(input("Enter c = "))

	delta = b*b-4*a*c


	if delta > 0:
		answer1 = b * (-1) / (a * 2) + math.sqrt(delta)
		answer2 = b * (-1) / (a * 2) - math.sqrt(delta)
		print("Two root: ", answer1, answer2)

	elif delta == 0:
		answer1 = b * (-1) / (a * 2) + math.sqrt(delta)
		print("Two root: ", answer1)
	else:
		print("No real roots")



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
