import os
import sys
import time
import json


def retrive_sample_data():
    file = open('players.json', 'r')
    result = json.load(file)
    file.close()
    return result


def dump_dict_to_json(my_data):
    with open("players.json", "a") as fp:
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
