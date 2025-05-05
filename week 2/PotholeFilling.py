"""
File: PotholeFilling.py
Name: Polly:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import*

def go_in():
    """
    pre-condition:Karel is at the upper left of the pothole, facing East
    post-condition:Karel is in the pothole, facing South
    """
    move()
    turn_right()
    move()

def turn_around():
    """
    pre-condition:Karel is in the hole,facing South
    post-condition:Karel is at the North East of the hole,facing East
    """
    turn_left()
    turn_left()
    move()
    turn_right()
    move()

def go_out():
    """
    pre-condition:Karel is in the pothole, facing South
    post-condition:Karel is at the upper left of the pothole, facing East
    """
    turn_around()

def main():
    """
    pre-condition:Karel is at (2,1),facing East
    post-condition:Karel is at (2,7),facing East
    """
    for i in range(3):
        go_in()
        put_karel_has_to_put_99_beepers()
        go_out()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
