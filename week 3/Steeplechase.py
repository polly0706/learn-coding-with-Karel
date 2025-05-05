"""
File: Steeplechase.py
Name: Polly
---------------------------------
TODO:
"""

from karel.stanfordkarel import *
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def up():
    """
    pre-condition:Karel is on the left side of the wall, facing East
    post-condition:Karel is at the upper left of the wall
    """
    #turn_left()
    #while not right_is_clear():
    #    move()

    #alternative
    while not front_is_clear():
        turn_left()
        move()
        turn_right()

def cross():
    """
    pre-condition:Karel is at the upper left of the wall
    post-condition:Karel is at the upper right of the wall
    """
    move()

def down():
    """
    pre-condition:Karel is at the upper right of the wall
    post-condition:Karel is on the right side of the wall
    """
    turn_right()
    while front_is_clear():
        move()
    turn_left()

def jump():
    """
    pre-condition:Karel is on the left side of the wall, facing East
    post-condition:Karel is on the right side of the wall
    """
    up()
    cross()
    down()

def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
            #jump()
        else:
            jump()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
