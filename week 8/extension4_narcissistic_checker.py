"""
File: extension4_narcissistic_checker.py
Name: Polly
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""

EXIT = -100

def main():
    print("Welcome to the narcissistic number checker!")
    enter = int(input("n:"))


    while enter != EXIT:
        sum = 0
        counter = 0
        standard = enter
        sum_enter = enter

        while enter != 0:
            #算幾位數
            while enter != 0:
                counter = counter + 1
                enter = enter // 10
            print(counter)

            #算總和
            while sum_enter != 0:
                a = sum_enter % 10
                print(a)
                sum = sum + a ** counter
                print(sum)
                sum_enter = sum_enter // 10
                print(sum_enter)

        #判斷總和是否為水仙花數
        if standard == sum:
            print(standard, "is a narcissistic number")
        else:
            print(standard, "is not a narcissistic number")
        enter = int(input("n:"))

    print("Have a good one!")



if __name__ == '__main__':
    main()
