from Text_functions import *
from Player import *
import time

TextFunction.play_sound_intro()
TextFunction.intro_message()
user = my_input('Do you want to play? Press \'y\'for yes and \'n\' for exit the game\n')
clear_screen()
if TextFunction.ask_if_play(user):
    user = my_input("""What character do you want to play:
                1. Wizard
                2. Warrior
                Please select 1 or 2.
                """)
    clear_screen()
    TextFunction.ask_type_of_char(user)
    time.sleep(1)
    clear_screen()
    if user == '1':
        user_name = my_input('Enter your name grand wizard: ')
        wizard = Wizard(user_name)
        my_print(f'Thank you wizard {wizard.name} for choosing to protect us')
    elif user == '2':
        user_name = my_input('Enter your name grand warrior: ')
        warrior = Warrior(user_name)
        my_print(f'Thank you wizard {warrior.name} for choosing to protect us')
    time.sleep(1)
    clear_screen()
    TextFunction.stop_sound()
    TextFunction.play_sound_exploring()
    user = my_input('''Now let's go to destroy our enemies.
            You have arrived on a crossword with 3 paths and you have to choose one!
            Please select 1, 2 or 3:
            1. To the forest
            2. To the town
            3. To the dungeon\n''')
    time.sleep(1)
    clear_screen()
    TextFunction.choosing_path(user)
