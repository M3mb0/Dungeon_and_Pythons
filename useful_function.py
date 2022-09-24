import os
import sys
import time


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


def play_again():
    user_answer = my_input("Do you want to play again? Y/N\n")
    clear_screen()
    if user_answer == 'y':
        return True
    else:
        my_print('''The realm needs you!!!
        Let's hope you will come back soon.''')
        return False
