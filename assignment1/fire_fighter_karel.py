from karel.stanfordkarel import *

# Author: Ali Fakhry
# Assignment #1 - fire_fighter_karel.py
# Date due: 2021-09-30
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

"""
File: fire_fighter_karel.py
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


def go_straight():
    """""

    While front is clear, move forward.

    Pre: Front is clear.

    Post: Karel will be facing a wall.

    """""

    while (front_is_clear()):
        while on_beeper():
            pick_beeper()
        move()


def left_clear():
    """""

    While front is clear, move forward.

    Pre: Left is clear.

    Post: Karel will no longer be to the left of a wall.

    """""

    turn_left()
    while (not right_is_clear() and front_is_clear()):
        while on_beeper():
            pick_beeper()
        move()


def hit_wall():
    """""

    Karel has hit a wall. Karel needs to turn around to continue to iterate through

    Pre: Hit wall. Karel is also blocked left and right.

    Post: Turn around (180). Then, move up.

    """""

    while on_beeper():
        pick_beeper()
    turn_around()
    if front_is_clear():
        move()


def go_through_fire_one_two():
    """""

    Iteration cycle for Karel to get through each "segment" as a firefighter.
    Karel must go through each of the three sides to pick up all the fire.
    This can be done through various ways. Such as being stuck in a 1x1 or by iterating through various turns.
    Regardless, these conditions allow Karel to do so well enough.

    YET, this definition is for the first two iterations out of the three. 

    Pre: None

    Post: At the end, Karel should have picked up all the fire.

    """""

    if front_is_clear():
        go_straight()
    if (left_is_clear()):
        turn_left()
    if front_is_clear():
        go_straight()
    if (left_is_clear()):
        left_clear()
    if (not right_is_clear() and not left_is_clear() and not front_is_clear()):
        hit_wall()
    if front_is_clear():
        move()
    if right_is_clear():
        turn_right()


def go_through_fire_three():
    """""

    Iteration cycle for Karel to get through each "segment" as a firefighter.
    Karel must go through each of the three sides to pick up all the fire.
    This can be done through various ways. Such as being stuck in a 1x1 or by iterating through various turns.
    Regardless, these conditions allow Karel to do so well enough.

    YET, this is used only for the LAST iteration. That is because Karel will have to stop at the end.
    Karel will NOT need the:

    if front_is_clear():
        move()
    if right_is_clear():
        turn_right()

    conditions. Karel must stop at the end.

    Pre: None

    Post: At the end, Karel should have picked up all the fire.

    """""

    if front_is_clear():
        go_straight()
    if (left_is_clear()):
        turn_left()
    if front_is_clear():
        go_straight()
    if (left_is_clear()):
        left_clear()
    if (not right_is_clear() and not left_is_clear() and not front_is_clear()):
        hit_wall()


def main():
    """
    The main function is used to start the first right turn and move.
    Then, the main function executes "go_through_fire_one_two" twice.
    Then, it executes "go_through_fire_three" one time.
    Go through first one/two has a slightly different ending than the last one.
    Thus, that is why there are two variations.
    """
    turn_right()
    move()

    go_through_fire_one_two()
    go_through_fire_one_two()
    go_through_fire_three()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
