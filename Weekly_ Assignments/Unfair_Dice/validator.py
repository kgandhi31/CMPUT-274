# ------------------------------------------------------------
# Name : Krish Gandhi
# ID: 1621641
# CMPUT 274, Fall 2020
#
# Weekly Exercise #1: Password Validator
# ------------------------------------------------------------

import random

# string with restricted characters
forbidden = [" ", "@", "#"]

# strings with requried character type
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
decimal = "0123456789"
special = "!-$%&'()*+,./:;<=>?_[]^`{|}~"


def validate(password):
    """ Analyzes an input password to determine if it is "Secure", "Insecure",
        or "Invalid" based on the assignment description criteria.

    Arguments:
        password (string): a string of characters inputted by the user

    Returns:
        result (string): either "Secure", "Insecure", or "Invalid".
    """

    # return "Invalid" if password is less than 8 characters in length
    if len(password) < 8:
        return("Invalid")

    # assume password does not contain all the required character types
    upper_exists = lower_exists = decimal_exists = special_exists = False

    # iterate through each character in password
    for char in password:

        # return "Invalid" if at least one forbidden character exists
        if char in forbidden:
            return ("Invalid")

        # check if all the required character types exist
        if char in upper:
            upper_exists = True
        if char in lower:
            lower_exists = True
        if char in decimal:
            decimal_exists = True
        if char in special:
            special_exists = True

    # return "Secure" if all required character types exist,
    # else return "Insecure"
    if upper_exists and lower_exists and decimal_exists and special_exists:
        return("Secure")
    else:
        return("Insecure")


def generate(n):
    """ Generates a password of length n which is guaranteed to be Secure
        according to the given criteria.

    Arguments:
        n (integer): the length of the password to generate, n >= 8.

    Returns:
        secure_password (string): a Secure password of length n.
    """

    # check if n is actually > 7
    if int(n) < 8:
        return("ERROR: NUMBER MUST BE GREATER THAN 7 TO GENERATE A PASSWORD!")

    password = ""

    # "infinite" loop that breaks when the length of the password is n
    while True:

        # list of all the required character types
        char_type_list = [upper, lower, decimal, special]

        # shuffle char_type_list on every while loop iteration
        random.shuffle(char_type_list)

        for type in char_type_list:

            # return the password if the length of the password equals n
            if len(password) == int(n):
                return(password)
            else:
                # add a random char from the type character string
                password += (random.choice(type))


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 validator.py". This is used to test the
    # implementation of the above functions.

    password = input("Please enter a password: ")
    print(validate(password))
    n = input("Please enter a number greater than 7: ")
    print(generate(n))
