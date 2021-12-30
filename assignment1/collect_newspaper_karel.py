from karel.stanfordkarel import *

# Author: Ali Fakhry
# Assignment #1 - collect_newspaper_karel.py
# Date due: 2021-09-30
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

"""
File: collect_newspaper_karel.py
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

def move_to_newspaper():

    """""

    Move Karel to the newspaper. 
    As there is only ONE world variation, this code is "step by step" and declarative.

    Pre: None.

    Post: Karel is on the beeper. 

    """""

    while front_is_clear():
        move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_left()
    move()

def pick_drop_newspaper():

    """""

    Karel has already picked up the beeper. Karel now has to drop off the newspaper.

    Pre: Karel has picked up the beeper/newspaper.

    Post: Karel has dropped off the beeper to the correct location.

    """""

    pick_beeper()
    turn_around()
    move()
    turn_right()
    move()
    move()
    turn_left()
    move()
    put_beeper()


def return_start():

    """""

    Move Karel back to the start of the world where Karel was.

    Pre: Karel has dropped the beeper.

    Post: Karel is back to the start. Facing the same direction as before.

    """""
    turn_right()
    move()
    move()
    turn_right()
    move()
    move()
    turn_right()


def main():
    """
    The main function here hosts three of the definitions which will sufficently allow Keral to pick up the
    newspaper.

    The first being "moveNewsPaper" which allows Keral to efficently move towards the newspaper.

    After that is accomplished, the second function/method is executed. This will allow Keral to bring the
    newspaper within the "house."

    Then, the offseting function "returnStart" will allow Keral to move back to where Keral was at the start.
    """
    move_to_newspaper()
    pick_drop_newspaper()
    return_start()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
