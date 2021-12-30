from karel.stanfordkarel import *

# Author: Ali Fakhry
# Assignment #1 - fill_pothole_karel.py
# Date due: 2021-09-30
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

"""
File: fill_pothole_karel.py
"""

def turn_around():

    """""

    Makes Karel turn around entirely.

    Pre: None.

    Post: Karel is turning the other way (180).

    """""

    turn_left()
    turn_left()


def turn_right():

    """""

    Makes Karel turn to the right. Turn left three times to do so.

    Pre: None.

    Post: Karel is turning the other way (90 degrees to the right).

    """""

    turn_left()
    turn_left()
    turn_left()

def fill_pothole():

    """""

    There is a hole to Karel's right. Karel needs to fill the hole.

    Pre: There is a hole to Karel's right. Right is NOT clear.

    Post: Karel's front is no longer clear. Went all the way.

    """""

    turn_right()
    while front_is_clear():
        move()
        if (not on_beeper()):
            put_beeper()
    go_back()

def go_back():

    """""

    Karel needs to leave the hole that Karel just filled. To do this, Karel needs to turn around and
    leave well. 

    Pre: Facing a wall. Front not clear.

    Post: Karel's right and left are clear. No longer "underground."

    """""

    turn_around()
    while (not left_is_clear() and not right_is_clear()):
        move()
    turn_right()
    if front_is_clear():
        move()

def main():

    """

    Karel starts facing east.
    Karel needs to continue going east way until blocked by a wall.
    Whenever there is a gap to the right (Kare's right), that indicates there is a hole to fill.

    The last case is that there is a gap to the right but Karel is facing a wall. In that case, Karel
    must still fill that hole.

    """

    while front_is_clear():
        if right_is_clear():
            fill_pothole()
        elif not right_is_clear():
            move()

    if (right_is_clear() and not front_is_clear()):
        fill_pothole()



####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
