
# Author: Ali Fakhry
# Assignment #3 - Blackjack
# Date due: 2021-10-28
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import random

FACE_CARD_VALUE = 10
ACE_VALUE = 1
CARD_LABELS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
BLACKJACK = 21
DEALER_THRESHOLD = 16

####### DO NOT EDIT ABOVE ########

def deal_card():
    """Evaluates to a character representing one of 13
    cards in the CARD_LABELS tuple
    :return: a single- or double-character string representing a playing card
    >>> random.seed(13)
    >>> deal_card()
    '5'
    >>> deal_card()
    '5'
    >>> deal_card()
    'J'
    """
    return(random.choice(CARD_LABELS))

def get_card_value(card_label):
    """Evaluates to the integer value associated with
    the card label (a single- or double-character string)
    :param card_label: a single- or double-character string representing a card
    :return: an int representing the card's value
    >>> card_label = 'A'
    >>> get_card_value(card_label)
    1
    >>> card_label = 'K'
    >>> get_card_value(card_label)
    10
    >>> card_label = '5'
    >>> get_card_value(card_label)
    5
    """
    if card_label == "A":
        return ACE_VALUE
    elif card_label == "J":
        return FACE_CARD_VALUE
    elif card_label == "Q":
        return FACE_CARD_VALUE
    elif card_label == "K":
        return FACE_CARD_VALUE
    else:
        return int(card_label)

def play_again():
    '''
    This function is used to ask the user if they wish to play again.
    :return: True if they want to play again. Return False if not.
    If they enter a value that does not match, the loop will restart after printing a blank line.
    '''
    user_input = ""
    while (user_input != "Y" and user_input !="N"):
        user_input = input("Play again (Y/N)?")
        if (user_input == "Y"):
            return True
        elif (user_input == "N"):
            return False
        else:
            print()

def get_player_input():
    '''
    Is used to retrive the player's input in regards to hit or stay.
    :return: True if they want to hit. Return False if not.
    If they enter a value that does not match, the loop will restart after printing a blank line.
    '''
    print()
    player_input = ""
    while(player_input != "h" and player_input != "s"):
        player_input = input("Hit (h) or Stay (s)?")
        if (player_input == "h"):
            return True
        elif (player_input == "s"):
            return False
        else:
            print()

def deal_cards_to_player():
    """Deals cards to the player and returns the card
    total
    :return: the total value of the cards dealt
    """
    random_card_one = deal_card()
    random_card_two = deal_card()

    print("Player drew {} and {}.".format(random_card_one, random_card_two))
    total_value = get_card_value(random_card_one) + get_card_value(random_card_two)
    print("Player's total is {}.".format(total_value))

    player_input = get_player_input()

    while (player_input == True):
        print()
        random_card_drawn = random.choice(CARD_LABELS)
        random_card_value = get_card_value(random_card_drawn)
        current_hold = total_value + random_card_value
        print("Player drew {}.".format(random_card_drawn))
        print("Player's total is {}.".format(current_hold))
        total_value += random_card_value
        if total_value < BLACKJACK:
            player_input = get_player_input()
        elif total_value >= BLACKJACK:
            return total_value

    print()
    return total_value

def deal_cards_to_dealer():
    """Deals cards to the player and returns the card
    total
    :return: the total value of the cards dealt
    """
    random_card_one = random.choice(CARD_LABELS)
    random_card_two = random.choice(CARD_LABELS)

    print("The dealer has {} and {}.".format(random_card_one, random_card_two))

    total_value = get_card_value(random_card_one) + get_card_value(random_card_two)

    print("Dealer's total is {}.".format(total_value))

    while (total_value <= DEALER_THRESHOLD):
        print()
        random_card_drawn = random.choice(CARD_LABELS)
        random_card_value = get_card_value(random_card_drawn)
        current_hold = total_value + random_card_value
        print("Dealer drew {}.".format(random_card_drawn))
        print("Dealer's total is {}.".format(current_hold))
        total_value += random_card_value

    return total_value

def determine_outcome(player_total, dealer_total):
    """Determines the outcome of the game based on the value of
    the cards received by the player and dealer. Outputs a
    message indicating whether the player wins or loses.
    :param player_total: total value of cards drawn by player
    :param dealer_total: total value of cards drawn by dealer
    :return: None
    """

    if (player_total == BLACKJACK and dealer_total == BLACKJACK):
        print("YOU LOSE!")
        print()

    elif (player_total > BLACKJACK):
        print("YOU LOSE!")
        print()

    elif (player_total <= BLACKJACK and dealer_total > BLACKJACK):
        print("YOU WIN!")
        print()

    elif (player_total > dealer_total):
        print("YOU WIN!")
        print()

    else:
        print("YOU LOSE!")
        print()

def play_blackjack():

    """Allows user to play Blackjack by making function calls for
    dealing cards to the player and the dealer as well as
    determining a game's outcome
    :return: None
    """

    running = True
    print("Let's Play Blackjack!")
    while(running):
        print()
        player_value = deal_cards_to_player()
        if (player_value > BLACKJACK):
            print()
            determine_outcome(player_value, 0)
        else:
            dealer_value = deal_cards_to_dealer()
            print()
            determine_outcome(player_value, dealer_value)

        check_play = play_again()
        if (check_play == True):
            pass
        else:
            print()
            print("Goodbye.")
            running = False


def main():
    """Runs a program for playing Blackjack with one player
    and a dealer
    """

    play_blackjack()

    # call play_blackjack() here and remove pass below
    pass


####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == "__main__":
    #Remove comments for next 4 lines to run doctests
    print("Running doctests...")
    import doctest
    doctest.testmod(verbose=True)

    print("\nRunning program...\n")

    main()