"""
File: CheckerboardKarel.py
Name: Polly
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def a_row_of_put_beeper():
    """
    pre-condition:Karel is at the top or bottom of the avenue,facing north or south
    post-condition:Karel is at the bottom or top of the avenue,facing north or south
    """
    while front_is_clear():
        if front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()


def wisely_uturn():
    #to identify whether to put beeper
    """
    pre-condition:
    post-condition:
    """
    if on_beeper():
        #7*7
        if facing_north():
            turn_right()
        if facing_south():
            turn_left()
        if front_is_clear():
            move()
            turn_right()
            move()
            if not on_beeper():
                put_beeper()

    else:
        #8*8
        if facing_north():
            turn_right()
        if facing_south():
            turn_left()
        if front_is_clear():
            move()
            put_beeper()
            turn_right()

def up():
    put_beeper()
    a_row_of_put_beeper()

def down():
    a_row_of_put_beeper()
    turn_left()
    if front_is_clear():
        move()

def last_check():
    turn_around()
    if not on_beeper():
        move()
        turn_left()
        put_beeper()
        a_row_of_put_beeper()


def turn_around():
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()

def main():
    if not front_is_clear():
        turn_left()
    while front_is_clear():
        if facing_east():
            turn_left()
        up()
        wisely_uturn()
        down()
    last_check()



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
