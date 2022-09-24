from Text_functions import *
from Player import *


Start.play_sound_intro()
Start.intro_message()
user = my_input('Do you want to play? Press \'y\'for yes and \'n\' for exit the game\n')
clear_screen()
if Start.ask_if_play(user):
    while play_again():
        user_char = my_input("""What character do you want to play:
                    1. Wizard
                    2. Warrior
                    Please select 1 or 2.
                    """)
        clear_screen()
        Start.ask_type_of_char(user_char)
        clear_screen()
        if user_char == '1':
            user_name = my_input('Enter your name grand wizard: ')
            wizard = Wizard(user_name)
            my_print(f'Thank you wizard {wizard.name} for choosing to protect us')
            clear_screen()
            Start.stop_sound()
            Start.play_sound_exploring()
            if Start.action():
                clear_screen()
                wizard.open_chest()
                my_print(f'You have found a wand with power of {wizard.weapon} and a robe with an armor of '
                         f'{wizard.armor}\n')
                wizard.gear_up()
                my_print(f'Your new power is {wizard.power} and your new armor is {wizard.defence}\n')
                Start.stop_sound()
                Start.play_sound_fight()
                enemy = Start.chose_enemy()
                while True:
                    wizard.attack(enemy)
                    my_print(f'You are attacking with a power of {wizard.power} your amor has {wizard.defence} '
                             f'durability left and {wizard.hp} HP left\n')
                    enemy.attack(wizard)
                    my_print(f'{enemy.type_of} is attacking you with a power of {enemy.power} and he has '
                             f'{enemy.critical}% '
                             f'chance to deal double damage. {enemy.type_of} armor has {enemy.defence} points and '
                             f'{enemy.hp} HP left\n')
                    if wizard.hp <= 0:
                        my_print(f'''Our wizard has been killed by a powerful {enemy.type_of}!!!
                        Rest in peace grand wizard\n''')
                        break
                    elif enemy.hp <= 0:
                        my_print(f'Well done grand wizard!!! You defeated the {enemy.type_of}\n')
                        break
            else:
                clear_screen()
                wizard.gear_up()
                my_print(f'Your power is {wizard.power} and your armor is {wizard.defence}\n')
                Start.stop_sound()
                Start.play_sound_fight()
                enemy = Start.chose_enemy()
                while True:
                    wizard.attack(enemy)
                    my_print(f'You are attacking with a power of {wizard.power} your amor has {wizard.defence} '
                             f'durability left and {wizard.hp} HP left\n')
                    enemy.attack(wizard)
                    my_print(f'{enemy.type_of} is attacking you with a power of {enemy.power} and he has '
                             f'{enemy.critical}% '
                             f'chance to deal double damage. {enemy.type_of} armor has {enemy.defence} points and '
                             f'{enemy.hp} HP left\n')
                    if wizard.hp <= 0:
                        my_print(f'''Our wizard has been killed by a powerful {enemy.type_of}!!!
                        Rest in peace grand wizard\n''')
                        break
                    elif enemy.hp <= 0:
                        my_print(f'Well done grand wizard!!! You defeated the {enemy.type_of}\n')
                        break
        elif user_char == '2':
            user_name = my_input('Enter your name grand warrior: ')
            warrior = Warrior(user_name)
            my_print(f'Thank you warrior {warrior.name} for choosing to protect us')
            clear_screen()
            Start.stop_sound()
            Start.play_sound_exploring()
            if Start.action():
                clear_screen()
                warrior.open_chest()
                my_print(f'You have found a sword with power of {warrior.weapon} and an armor with a durability of '
                         f'{warrior.armor}\n')
                warrior.gear_up()
                my_print(f'Your new power is {warrior.power} and your new armor is {warrior.defence}\n')
                Start.stop_sound()
                Start.play_sound_fight()
                enemy = Start.chose_enemy()
                while True:
                    warrior.attack(enemy)
                    my_print(f'You are attacking with a power of {warrior.power} your amor has {warrior.defence} '
                             f'durability left and {warrior.hp} HP left\n')
                    enemy.attack(warrior)
                    my_print(f'{enemy.type_of} is attacking you with a power of {enemy.power} and he has '
                             f'{enemy.critical}% '
                             f'chance to deal double damage. {enemy.type_of} armor has {enemy.defence} points and '
                             f'{enemy.hp} HP left\n')
                    if warrior.hp <= 0:
                        my_print(f'''Our warrior has been killed by a powerful {enemy.type_of}!!!
                        Rest in peace grand wizard\n''')
                        break
                    elif enemy.hp <= 0:
                        my_print(f'Well done grand warrior!!! You defeated the {enemy.type_of}\n')
                        break
            else:
                clear_screen()
                warrior.gear_up()
                my_print(f'Your power is {warrior.power} and your armor is {warrior.defence}\n')
                Start.stop_sound()
                Start.play_sound_fight()
                enemy = Start.chose_enemy()
                while True:
                    warrior.attack(enemy)
                    my_print(f'You are attacking with a power of {warrior.power} your amor has {warrior.defence} '
                             f'durability left and {warrior.hp} HP left\n')
                    enemy.attack(warrior)
                    my_print(f'{enemy.type_of} is attacking you with a power of {enemy.power} and he has '
                             f'{enemy.critical}% '
                             f'chance to deal double damage. {enemy.type_of} armor has {enemy.defence} points and '
                             f'{enemy.hp} HP left\n')
                    if warrior.hp <= 0:
                        my_print(f'''Our warrior has been killed by a powerful {enemy.type_of}!!!
                        Rest in peace grand wizard\n''')
                        break
                    elif enemy.hp <= 0:
                        my_print(f'Well done grand warrior!!! You defeated the {enemy.type_of}\n')
                        break
