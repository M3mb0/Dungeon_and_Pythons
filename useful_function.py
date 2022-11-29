"""Functions that are give some design functionality to the script and contain:

Function:
    --------------
    save_data:
        Function saves the player data in json file
    my_print:
        Overwrite the print function
    my_input:
        Overwrite the input function
    clear_screen:
        Clears the screen

Other imports:
    --------------
    os:
        used in clear_screen function
    sys:
        used in my_input and my_print functions
    time:
        used in all functions except save_date
    json:
        used in save_data function

"""

import os
import sys
import time
import json


def save_data(my_data):
    """Writes the player stats in a json file and takes 1 argument.

    Argument:
    --------------
        my_data: var -> str, int
            Variable taken from a dictionary.
    """
    with open("players.json", "w") as fin:
        json.dump(my_data, fin, indent=4)


def my_print(text):
    """Overwrites the print function by printing character after character
    with a delay of 0.05 seconds. Function takes 1 argument.

    Argument:
    --------------
        text: str
            plain text
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def my_input(text):
    """Overwrites the input function by printing character after character
    with a delay of 0.05 seconds. Function takes 1 argument and
    returns the value which is the input entered by the user.

    Argument:
    --------------
        text: str
            plain text
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


def clear_screen():
    """Clears the screen when is called with a delay of 1 second and takes no arguments"""
    time.sleep(1)
    os.system('cls')
