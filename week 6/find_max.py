"""
File: find_max.py
Name:Polly
--------------------------
This program finds the maximum among
all the user inputs. Students can refer to
this file when they are doing Problem 4
in Assignment 2
"""

# This constant controls when to stop
EXIT = -1


def main():
    """
    This program finds the maximum among
    user inputs
    """
    print("找最大值")
    data = int(input("數據: "))

    if data == EXIT:
        print("no data")
    else:
        maximum = data
        while data != -1:
            if maximum < data:
                maximum = data
            data = int(input("數據: "))
        print("最大值是:", str(maximum))



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
