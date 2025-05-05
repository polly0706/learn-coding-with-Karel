"""
File: receipt.py
Name:
-------------------------
This program calculates the meal cost
and prints the result on Console.
Students will learn variables, user inputs,
and concatenation
"""


def main():
    meal = int(input("餐費: "))
    tax_money = float(input("稅: "))
    total = meal * (1 + tax_money)
    print("總和: ", str(total),"!")


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
