"""
File: scores_classifier
Name: Polly
--------------------------------------
This program classifies scores into 4 catagories:
90 up: A
80 up: B
70 up: C
below 70: D
"""

def main():
    scores = int(input("分數:"))
    if scores >= 90:
        print("A")
    elif scores >= 80:
        print("B")
    elif scores >= 80:
        print("C")
    else:
        print("D")


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()