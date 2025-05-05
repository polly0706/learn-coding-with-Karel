"""
File: extension3_triangular_checker.py
Name:Polly
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""

EXIT = -100

def main():
    print("Welcome to the triangular number checker!")
    enter = int(input("n:"))
    sum = 0
    a = 0

    while enter != EXIT:
        #加到超過(或等於)
        while enter > sum:
            sum = sum + a
            a += 1
        if enter == sum:
            print(enter, "is a triangular number")
        else:
            print(enter, "is not a triangular number")
        enter = int(input("n:"))

    print("Have a good one!")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
