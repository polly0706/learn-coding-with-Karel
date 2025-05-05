"""
File: CollectNewspaperKarel.py
Name: Polly
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go():
    """
    pre-condition:Karel is at Street 4,Avenue 3,facing East
    post-condition:Karel is at Street 3,Avenue 6,facing East
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()

def back():
    """
    pre-condition:Karel is at Street 3,Avenue 6,facing East
    post-condition:Karel is at Street 4,Avenue 3,facing East
    """
    turn_left()
    turn_left()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_left()
    turn_left()

def main():
    go()
    pick_beeper()
    back()
    put_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
