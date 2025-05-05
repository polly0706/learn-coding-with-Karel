"""
File: guess_my_number.py
Name:
-----------------------------
This program plays a Console game
"Guess My Number" which asks user
to input a number until he/she gets it
"""

# This number controls when to stop the game
SECRET = 32


def main():
    print("猜 0~99: ")
    while True:
        guess = int(input("your guess: "))
        if guess > SECRET:
            print("太高了")
        elif guess == SECRET:
            break
        else:
            print("太低了")
    print("恭喜~~答案是:", str(SECRET))




"""
    guess = int(input("請猜一個整數: "))

    while guess != SECRET:
        if guess > SECRET:
            print("太大了，現在區間: 0~", str(guess))
        else:
            print("太小了，現在區間: ", str(guess), "~99")
        guess = int(input("請猜一個整數: "))
    print("猜對了~~~")
"""

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
