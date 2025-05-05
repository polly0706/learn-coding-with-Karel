"""
File: MidpointKarel.py
Name: Polly
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *

def u_turn():
    turn_left()
    turn_left()

def main():
    #put beeper at the two side of the street first
    put_beeper()
    move()
    while front_is_clear():
        move()
    put_beeper()
    u_turn()
    move()

    #then move beeper to the forward spot until it overlap
    while not on_beeper():
        while not on_beeper():
            move()
        u_turn()
        pick_beeper()
        move()
        put_beeper()
        move()
    pick_beeper()

    #make sure it only leave one beeper
    turn_left()
    if front_is_clear():
        move()
    else:
        turn_left()
        turn_left()
        move()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
