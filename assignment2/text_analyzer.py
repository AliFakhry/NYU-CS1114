# Author: Ali Fakhry
# Assignment #2 - TextAnalyzer
# Date due: 2021-10-14
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

####### DO NOT EDIT FUNCTIONS BELOW ########

def character_is_digit(char):
    """Indicates whether the value referenced by char parameter
    is a digit character

    :param char: character to check
    :return: True when char is a digit character, False otherwise

    >>> test_char = 'b'
    >>> character_is_digit(test_char)
    False
    >>> test_char = '2'
    >>> character_is_digit(test_char)
    True
    """

    return char.isdigit()


def character_is_letter(char):
    """Indicates whether the value referenced by char parameter
    is a letter

    :param char: character to check
    :return: True when char is a letter, False otherwise

    >>> test_char = 'b'
    >>> character_is_letter(test_char)
    True
    >>> test_char = '2'
    >>> character_is_letter(test_char)
    False
    """

    return char.isalpha()

def character_is_whitespace(char):
    """Indicates whether the value referenced by char parameter
    is a whitespace character (' ', '\n', '\t')
    :param char: character to check
    :return: True when char is space character, False otherwise
    """
    if (char == ' '):
        return True
    elif (char == '\n'):
        return True
    elif (char == '\t'):
        return True
    else:
        return False

def character_ends_sentence(char):
    """Indicates whether the value referenced by char parameter
    is a period, question mark, or exclamation point
    :param char: character to check
    :return: True when char ends sentence, False otherwise
    """
    if (char == '.'):
        return True
    elif (char == '?'):
        return True
    elif (char == '!'):
        return True
    else:
        return False

def good_bye():
    '''
    Prints goodbye
    :return None:
    '''
    print("\n")
    print("Goodbye.")

def print_results(num_chars, num_spaces, num_digits, num_letters, num_sentences):
    '''
    Prints the number of total characters, spaces, digits, letters,
    and sentences identified in the text being analyzed.
    :param num_chars: number of total characters in text
    :param num_spaces: number of spaces in text
    :param num_digits: number of digits in text
    :param num_letters: number of letters in text
    :param num_sentences: number of sentences in text
    :return: None
    '''

    print()
    print("Number of characters: " + str(num_chars))
    print("Number of spaces: "+ str(num_spaces))
    print("Number of digits: " + str(num_digits))
    print("Number of letters: " + str(num_letters))
    print("Number of sentences: " + str(num_sentences))
    print()

def run_text_analyzer():
    """Runs the Text Analyzer as a repeated sequence of
    prompting the user for input text and outputting the
    character counts computed from the input
    :return: None
    """

    print ("Welcome to the Text Analyzer!")
    running_function = True
    while(running_function):
        user_input = input("Please enter text to analyze (press ENTER/return without text to exit):")
        return_value = analyze_text(user_input)
        if (return_value == True):
            pass
        elif (return_value == False):
            good_bye()
            running_function = False

def analyze_text(user_input):
    """Calls the functions to compute the number of total characters,
    spaces, digits, letters, and sentences in user-supplied text and to
    output the final counts when text input by user.
    :return: True when text provided, False when no text provided
    """
    returning_statement = None
    num_chars, num_spaces, num_digits, num_letters, num_sentences = 0, 0, 0, 0, 0
    if (user_input == ""):
        return False
    else:
        returning_statement = True
        for i in user_input:
            num_chars += 1
            if (character_is_whitespace(i)):
                num_spaces += 1
            elif (character_is_letter(i)):
                num_letters += 1
            elif (character_is_digit(i)):
                num_digits += 1
            elif (character_ends_sentence(i)):
                num_sentences+= 1

        print_results(num_chars, num_spaces, num_digits, num_letters, num_sentences)
        return returning_statement

####### DO NOT EDIT FUNCTIONS ABOVE ########

def main():
    """Runs a program for analyzing character counts from
    input text

    Runs "run_text_analyzer()"
    """

    run_text_analyzer()


    # call run_text_analyzer() here and remove pass below
    pass

    
####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == '__main__':
    # Remove comments for next 4 lines to run doctests
    # print("Running doctests...")
    # import doctest
    # doctest.testmod(verbose=True)

    # print("\nRunning program...\n")

    main()
