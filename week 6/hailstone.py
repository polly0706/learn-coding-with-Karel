"""
File: hailstone.py
Name:
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    print("This program computes Hailstone  sequence.")
    print("\n")
    mystery = int(input("Enter a number: "))
    counter = 0

    if mystery == 1:
        print("It took 0 steps to reach 1.")
    else:
        while mystery != 1:
            if mystery %2 == 1:
                answer = mystery *3 +1
                print(str(int(mystery)), "is odd,", "so I take 3n+1: ", int(answer))
            else:
                answer = mystery /2
                print(str(int(mystery)), "is even,", "so I take half: ", int(answer))
            mystery= answer
            counter += 1
        print("It took", str(counter), " steps to reach 1.")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
