import os
import sys
import time
import json


def save_data(my_data):
    with open("players.json", "w") as fp:
        json.dump(my_data, fp, indent=4)


def my_print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def my_input(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


def clear_screen():
    time.sleep(1)
    os.system('cls')
