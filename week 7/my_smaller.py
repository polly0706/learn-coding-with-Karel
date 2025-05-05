"""
File: my_smaller.py
Name:
-------------------------
This program implements a my_smaller function
which takes 2 arguments and outputs the
smaller one
"""


def main():
    """
    Call my_smaller function
    """
    n1 = int(input('First Number: '))
    n2 = int(input('Second Number: '))
    smaller = my_smaller(n1, n2)
    print(smaller)
    sum = my_add(n1,n2)
    print(sum)


def my_smaller(n1, n2):
    """
    :param n1: int
    :param n2: int
    :return: int
    """
    if n1 < n2:
        return n1
    return n2  #return 會終止function

def my_add(n1,n2):
    """
    n1: int
    n2: int
    return: int
    """
    ans = n1 + n2
    return ans


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
