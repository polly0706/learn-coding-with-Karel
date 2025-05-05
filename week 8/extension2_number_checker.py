"""
File: extension2_number_checker.py
Name: Polly
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""


EXIT = -100

def main():
    print("Welcome to the number checker!")

    enter = int(input("n:"))


    while enter != EXIT:
        a = 1
        sum = 0
        while a < enter:
            if enter % a == 0:
                sum = sum + a
            a += 1

        if sum == enter:
            print(enter, "is a perfect number")
        elif sum > enter:
            print(enter, "is an abundant number")
        else:
            print(enter, "is a deficient number")

        enter = int(input("n:"))

    print("Have a good one!")

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
