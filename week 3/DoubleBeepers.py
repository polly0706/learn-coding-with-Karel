"""
File: DoubleBeepers.py
Name:Polly
-------------------------------
TODO:
"""

from karel.stanfordkarel import *

def back_to_start():
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()

def double_beeper():

    move()
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        back_to_start()

def put_beeper_to_start():
    while on_beeper():
        pick_beeper()
        back_to_start()
        put_beeper()
        move()


def main():
    """
    Karel will double the beepers
    """
    double_beeper()
    move()
    put_beeper_to_start()




# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
