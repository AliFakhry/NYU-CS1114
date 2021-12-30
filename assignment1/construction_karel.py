from karel.stanfordkarel import *

# Author: Ali Fakhry
# Assignment #1 - construction_karel.py
# Date due: 2021-09-30
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

"""
File: construction_karel.py
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

def build_tower():

    """""

    Finish building the tower.

    Pre: Karel is on a beeper.

    Post: The tower at the current vertical has a height of three.

    """""

    turn_left()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_around()
    move()
    move()
    turn_left()
    move()

def check_beeper():

    """""

    Check if Karel is on a beeper.

    Pre: None.

    Post: Two results: move forward no beeper. If beeper, build the tower.

    """""

    if not on_beeper():
        move()
    elif on_beeper():
        build_tower()

def main():

    """
    Karel starts at a horizontal of 1. Karel must end at a horizontal of 5.
    Thus, check beeper 4 times as that is the maximum number of possible constructions that need to be completed.
    """

    check_beeper()
    check_beeper()
    check_beeper()
    check_beeper()

####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
