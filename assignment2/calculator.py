# Author: Ali Fakhry
# Assignment #2 - Calculator
# Date due: 2021-10-14
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

def do_addition():
    """Informs user that addition was chosen, sums two
    numbers input by the user, and outputs the result.
    :return: None
    """
    print()
    print("You have chosen the addition operation.")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    add_result = num1 + num2
    print("The sum is:", add_result)

def do_subtraction():
    """Informs user that subtraction was chosen, calculates
    the difference between two numbers input by the user, and
    outputs the result.
    :return: None
    """
    print()
    print("You have chosen the subtraction operation.")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    subtract_number = num1 - num2
    print(subtract_number)

def do_multiplication():
    """Informs user that multiplication was chosen, multiplies two
    numbers input by the user, and outputs the result.
    :return: None
    """

    print()
    print("You have chosen the multiplication.")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    multiplication_number = num1 * num2
    print("The product is", multiplication_number)

def do_division():

    """Informs user that division was chosen, divides two
    numbers input by the user, and outputs the result.
    :return: None
    """
    print()
    print("You have chosen the division operation.")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    division_number = num1 / num2
    print("The result of the division of the two numbers is" , division_number)

def do_quit():
    '''
    Prints Goodbye
    :return None:
    '''
    print()
    print("Goodbye.")

def do_calculation(user_input):

    if ((user_input) == "1"):
        do_addition()

    elif ((user_input) == "2"):
        do_subtraction()

    elif ((user_input) == "3"):
        do_multiplication()

    elif ((user_input) == "4"):
        do_division()
    else:
        print("That was not a valid choice. Try again.")

    return user_input

def print_menu():
    """Prints available calculator operations.
       :return: None
       >>> print_menu()
       <BLANKLINE>
       1) Perform addition
       2) Perform subtraction
       3) Perform multiplication
       4) Perform division
   """
    print()
    print(
        "1) Perform addition\n" +
        "2) Perform subtraction\n" +
        "3) Perform multiplication\n" +
        "4) Perform division"
    )

def run_calculator():
    """Runs the calculator as a repeated sequence of
    displaying the calculator menu and performing a
    calculation based on the user's choice.
    :return: None
    """
    print("Welcome to the CS 1114 Calculator!")
    running_function = True
    while(running_function):
        print_menu()
        user_input = input("Please enter an option (1-4) or ’q’ to quit: ")
        if user_input == "q":
            do_quit()
            running_function = False
        else:
            do_calculation(user_input)

def main():
    """Runs a program for performing basic arithmetic
    operations between two numbers
    """

    run_calculator()

    pass


####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == '__main__':
    # Remove comments for next 4 lines to run doctests
    # print("Running doctests...")
    # import doctest
    # doctest.testmod(verbose=True)

    # print("\nRunning program...\n")

    main()
