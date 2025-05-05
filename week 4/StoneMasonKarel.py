"""
File: StoneMasonKarel.py
Name: Polly
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def cross():
    """
    pre-condition:Karel is at somewhere of the world
    post-condition:Karel is 4 steps forward than pre-condition
    """
    for i in range(4):
        move()


def wall_fixing():
    """
    pre-condition:Karel is facing North
    post-condition:Karel is 5 steps forward than pre-condition,facing North
    """
    for i in range(5):
        if not on_beeper():
            put_beeper()
        if front_is_clear():
            move()


def one_house_fixing():
    """
    pre-condition:Karel is facing East
    post-condition:Karel is 4 steps forward than pre-condition,facing East
    """
    turn_left()
    wall_fixing()
    turn_right()
    cross()
    turn_right()
    wall_fixing()
    turn_left()

def last_check():
    """
    pre-condition:Karel is at the bottom of the last wall
    post-condition:Karel is at the top of the last wall
    """
    turn_left()
    wall_fixing()

def back_to_the_end():
    """
    pre-condition:Karel is at the top of the last wall
    post-condition:Karel is at the bottom of the last wall
    """
    turn_right()
    turn_right()
    cross()
    turn_left()

def main():
    while front_is_clear():
        one_house_fixing()
        if front_is_clear():
            cross()
    last_check()
    back_to_the_end()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
