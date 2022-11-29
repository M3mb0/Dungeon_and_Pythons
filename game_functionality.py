"""This modul offers the game functionality and contain the fallowing

Class:
    --------------
    Game:
        A class with static methods only and takes no arguments.
Method:
    --------------
    stop_sound:
        stops the sounds from the game
    play_sound_intro:
        playing the intro music(main menu)
    play_sound_exploring:
        playing the exploring music(after the game starts)
    play_sound_fight:
        playing the fighting music(when the fight begins)
    intro_message:
        prints the intro message
    wizard_message:
        prints a descriptions of the wizard
    knight_message:
        prints a descriptions of the knight
    play_again:
        ask the player if he wants to play again and return True or False
    game:
        ask the user to choose a character and starts the exploring and fighting scene
    game_intro:
        prints the main menu and returns True or False
    continue_fighting:
        getting player data and stats from json to continue his game
    get_char_info:
        getting char info and stats from json
    ask_user_name:
        ask the user to input his name and save it to json
    ask_type_of_char:
        ask the user to choose the type of character he wants to play
    choosing_path:
        prints the story of every path
    action:
        print the paths and the chest story
    chose_enemy:
        choosing an random enemy for the fighting scene and returns it
    player_no_chest:
        equip the player with his default weapon and armor and save the data in json
    player_open_chest:
        equip the player with the found weapon and armor and save data to json
    battle:
        starts the battle between the player and the enemy and prints the action
    boss_fight:
        starts the boss fight
    fighting_scene:
        starts the fighting scene after the player choice of opening or not the chest
    main_battle:
        runs the battle in a loop, until one of the players run out of hp
    increase_player_level:
        increase the player stats if he has enough xp,
        by getting data from json and overwrite it if level up
    save_data_warrior:
        store the player data and stats in a json file and returns it
Function and variables:
    --------------
    USER_PARAM:
        empty dictionary
    retrieve_sample_data:
        function that reads data from json file
Other imports:
    --------------
    json:
        for writing and reading json files
    random:
        for geting an random enemy from a list
    winsound:
        used to play music during the game
    enemy:
        importing Goblin, Orc, Troll, Python classes to create the enemy objects
    player:
        importing Wizard, Knight classes to create the players objects
    useful_function:
        importing save_data, my_print, my_input, clear_screen to give a better design to the game
"""

import json
import random
import winsound

from enemy import Goblin, Orc, Troll, Python
from player import Wizard, Knight
from useful_function import save_data, my_print, my_input, clear_screen

USER_PARAM = {}


def retrieve_sample_data():
    """reading the json file and assign it to a global variable"""
    global USER_PARAM
    file = open('players.json', 'r')
    USER_PARAM = json.load(file)
    file.close()


retrieve_sample_data()


class Game:
    """A class with static methods only and takes no arguments.
Method:
    --------------
    stop_sound:
        stops the sounds from the game
    play_sound_intro:
        playing the intro music(main menu)
    play_sound_exploring:
        playing the exploring music(after the game starts)
    play_sound_fight:
        playing the fighting music(when the fight begins)
    intro_message:
        prints the intro message
    wizard_message:
        prints a descriptions of the wizard
    knight_message:
        prints a descriptions of the knight
    play_again:
        ask the player if he wants to play again and return True or False
    game:
        ask the user to choose a character and starts the exploring and fighting scene
    game_intro:
        prints the main menu and returns True or False
    continue_fighting:
        getting player data and stats from json to continue his game
    get_char_info:
        getting char info and stats from json
    ask_user_name:
        ask the user to input his name and save it to json
    ask_type_of_char:
        ask the user to choose the type of character he wants to play
    choosing_path:
        prints the story of every path
    action:
        print the paths and the chest story
    chose_enemy:
        choosing an random enemy for the fighting scene and returns it
    player_no_chest:
        equip the player with his default weapon and armor and save the data in json
    player_open_chest:
        equip the player with the found weapon and armor and save data to json
    battle:
        starts the battle between the player and the enemy and prints the action
    boss_fight:
        starts the boss fight
    fighting_scene:
        starts the fighting scene after the player choice of opening or not the chest
    main_battle:
        runs the battle in a loop, until one of the players run out of hp
    increase_player_level:
        increase the player stats if he has enough xp,
        by getting data from json and overwrite it if level up
    save_data_warrior:
        store the player data and stats in a json file and returns it"""

    @staticmethod
    def stop_sound():
        """Stop the music in the game and take no arguments"""
        winsound.PlaySound(None, winsound.SND_PURGE)

    @staticmethod
    def play_sound_intro():
        """Start the intro music and take no arguments"""
        winsound.PlaySound("Music_Game/Main_Menu.wav", winsound.SND_ASYNC + winsound.SND_LOOP)

    @staticmethod
    def play_sound_exploring():
        """Start the exploring music and take no arguments"""
        winsound.PlaySound("Music_Game/Exploring.wav", winsound.SND_ASYNC + winsound.SND_LOOP)

    @staticmethod
    def play_sound_fight():
        """Start the fight music and take no arguments"""
        winsound.PlaySound("Music_Game/BattleFinal.wav", winsound.SND_ASYNC + winsound.SND_LOOP)

    @staticmethod
    def intro_message():
        """Prints the intro message and takes no arguments"""
        my_print("""Welcome stranger.
          ->  Here in Hinterlands, you'll get
          to fight strong opponents and
          conquer the deadliest dungeons.
          ->  In a country
          where magic rules,
          anything is possible if
          you wish so.
          ->  It all depends
        """)

    @staticmethod
    def wizard_message():
        """Prints the wizard story and takes no arguments"""
        my_print("""Congratulations, grand wizard!
          ->  Wizards were
          the scholars of 
          Hinterlands,
          spreading knowledge
          and hope amongst
          the people.
          ->  Are you going 
          to help and nurture
          those in need, or turn ? 
        """)

    @staticmethod
    def knight_message():
        """Prints the knight story and takes no arguments"""
        my_print("""Congratulations, great knight!
          ->  Knights were
          high regarded in
          Hinterlands,as they
          were the only
          protectors of common
          folks.
          ->  Are you going
          to protect the
          common people, or turn? 
        """)

    @staticmethod
    def play_again():
        """Continue or closing the game based on the user choice and takes no arguments.
        Returns True if user wants to play again or False if he doesn't"""
        user_answer = my_input("""Do you want to play again?
        Press \'y\' to play or press any key to leave the game\n""")
        clear_screen()
        if user_answer == 'y':
            return True
        else:
            my_print('''The realm needs you!!!
            Let's hope you will come back soon.''')
            return False

    @staticmethod
    def game():
        """Ask the user to choose a character and starts the exploring and fighting scene
        and takes no arguments.
        It also creates the characters based on user choice"""
        user_char = my_input(f"""
        What character do you want to play {USER_PARAM.get('name')}:
                            1. Wizard
                            2. Knight
        Please select 1 or 2 
        (If you press any another key, you will play as Knight by default).\n""")
        clear_screen()
        Game.ask_type_of_char(user_char)
        clear_screen()
        if user_char == '1':
            wizard = Wizard(USER_PARAM.get('name'))
            Game.save_data_warrior(wizard)
            my_print(f'Thank you wizard {wizard.name} for choosing to protect us')
            Game.fighting_scene(wizard)
        else:
            knight = Knight(USER_PARAM.get('name'))
            Game.save_data_warrior(knight)
            my_print(f'Thank you Sir {knight.name} for choosing to protect us')
            Game.fighting_scene(knight)

    @staticmethod
    def game_intro():
        """Prints the main menu and is taking no arguments
        Starting the game, based on the user input and returns True
        if players wants to play or False if he doesn't"""
        Game.play_sound_intro()
        Game.intro_message()
        clear_screen()
        user = my_input('''What do you want to do?
        1. Start a new game
        2. Continue
        3. Exit
        Please select 1,2 or 3
        (If you type any other key you will exit the game!)\n''')
        clear_screen()
        if user == '1':
            my_print("""Great!
            Let's fight for this realm!
        """)
            Game.ask_user_name()
            Game.game()
            return True
        elif user == '2':
            Game.continue_fighting()
            return True
        else:
            my_print('Hope you will come back soon.The land needs you')
            return False

    @staticmethod
    def continue_fighting():
        """Getting player data and stats from json to continue his game,
         and it takes no arguments
        Creating new character objects based on what is stored in json file."""
        if USER_PARAM.get("type_of") == "wizard":
            wizard = Wizard(USER_PARAM.get("name"))
            Game.get_char_info(wizard)
            Game.fighting_scene(wizard)
        elif USER_PARAM.get("type_of") == "knight":
            knight = Knight(USER_PARAM.get("name"))
            Game.get_char_info(knight)
            Game.fighting_scene(knight)

    @staticmethod
    def get_char_info(char):
        """Reading the data stored in json and is taking 1 argument.

        Argument:
        --------------
            char: obj
                character chosen by the player
        """
        char.name = USER_PARAM.get('name')
        char.level = USER_PARAM.get('level')
        char.experience = USER_PARAM.get('experience')
        char.type_of = USER_PARAM.get('type_of')
        char.hp = USER_PARAM.get('hp')
        char.defence = USER_PARAM.get('defence')
        char.power = USER_PARAM.get('power')
        char.weapon = USER_PARAM.get('weapon')
        char.armor = USER_PARAM.get('armor')

    @staticmethod
    def ask_user_name():
        """Asks the users name and store it to a json file,
        and it takes no arguments"""
        user = my_input('Please enter your name brave warrior: ')
        USER_PARAM['name'] = user
        save_data(USER_PARAM)
        clear_screen()

    @staticmethod
    def ask_type_of_char(user):
        """Prints the character story based on user choice and takes 1 argument

        Argument:
        --------------
            char: obj
                player character
        """
        if user == '1':
            Game.wizard_message()
        else:
            Game.knight_message()

    @staticmethod
    def choosing_path(user):
        """Prints the story of the path based on user input and takes 1 argument

        Argument:
        --------------
            char: obj
                player character
        """
        if user == '1':
            my_print('''
            A lot of brave heroes entered in this forest but only a few came back!
            Strange creatures stalk you so be aware!
            In this forest you can find hidden chests with powerful items 
            so be sure to collect them
            ''')
        elif user == '2':
            my_print('''
            This town is now ruled by some scary creatures and all humans were kill by them.
            So keep an eye out!
            In this town you can find hidden chests with powerful items 
            so be sure to collect them
            ''')
        else:
            my_print('''
            Dungeons are probably the scariest and you have to be aware at every sound,
            otherwise you might be taken by surprise.
            In this dungeon you can find hidden chests with powerful items 
            so be sure to collect them
            ''')

    @staticmethod
    def action():
        """Asking the user to choose a path and after that
        is asked if he wants to open the chest that he found.
        Method takes no arguments.
        Based of user choice the method returns True if the user wants to open the chest
        or False if he doesn't"""
        user_path = my_input('''Now let's go to destroy our enemies.
                        You have arrived on a crossroad with 3 paths and you have to choose one!
                        1. To the forest
                        2. To the town
                        3. To the dungeon
        Please select 1, 2 or 3
        (if you press any other key, you will go to the dungeon by default) \n''')
        clear_screen()
        Game.choosing_path(user_path)
        clear_screen()
        user_risk = my_input('''You have found a chest!
                You can choose to open it and getting a better or worse weapon and armor
                or you can leave it and fight using your own items.
                What it will be?
                Do you risk or not?
        Type \'y\' to risk or press any key to keep your items\n''')
        if user_risk == 'y':
            return True
        else:
            return False

    @staticmethod
    def chose_enemy():
        """Creating the enemy objects, withdraw a random enemy and returns it
        The method is taking no arguments"""
        goblin = Goblin()
        orc = Orc()
        troll = Troll()
        enemy_list = [goblin, orc, troll]
        enemy = random.choice(enemy_list)
        my_print(f'Your opponent is an {enemy.type_of} and has {enemy.hp} HP, {enemy.defence}'
                 f' defence points and he hits with a power of {enemy.power}\n')
        clear_screen()
        return enemy

    @staticmethod
    def player_no_chest(char):
        """Equip the player with his default weapon and armor if player
        does not open the chest and save his stats in a json file.
        Method takes 1 argument.

        Argument:
        --------------
            char: obj
                player character
        """
        clear_screen()
        char.gear_up()
        Game.save_data_warrior(char)
        my_print(f'Your power is {char.power} and your armor is {char.defence}\n')
        Game.stop_sound()
        Game.play_sound_fight()

    @staticmethod
    def player_open_chest(char):
        """Equip the player with the weapon and armor found in the chest and save data to json.
        Method takes 1 argument.

        Argument:
        --------------
            char: obj
                player character
        """
        clear_screen()
        char.open_chest()
        Game.save_data_warrior(char)
        my_print(f'You have found a {char.weapon_type} with power of {char.weapon} and '
                 f'a {char.armor_type} '
                 f'with extra defence of {char.armor}\n')
        char.gear_up()
        Game.save_data_warrior(char)
        my_print(f'Your new power is {char.power} and your new armor is {char.defence}\n')
        Game.stop_sound()
        Game.play_sound_fight()

    @staticmethod
    def battle(enemy, char):
        """Starts the battle between the player and the enemy and prints the action
        Method takes 2 arguments.

        Argument:
        --------------
            char: obj
                player character
            enemy: obj
                enemy character
        """
        char.attack(enemy)
        my_print(f'You are attacking with a power of {char.power}, your amor has {char.defence} '
                 f'durability and {char.hp} HP left.\n')
        enemy.attack(char)
        my_print(f'{enemy.type_of} is attacking you with a power of {enemy.power} and he has '
                 f'{enemy.critical}% '
                 f'chance to deal double damage. {enemy.type_of} '
                 f'armor has {enemy.defence} points and '
                 f'{enemy.hp} HP left\n')
        if enemy.hp <= 0:
            my_print(f'Well done grand {char.type_of}!!! You defeated the {enemy.type_of}\n')
            char.hp = USER_PARAM.get('hp')
            char.defence = USER_PARAM.get('defence')
            Game.increase_player_level(char, enemy)
        elif char.hp <= 0:
            my_print(f'''Our {char.type_of} has been killed by a powerful {enemy.type_of}!!!
                            Rest in peace grand {char.type_of}\n''')

    @staticmethod
    def boss_fight(boss, char):
        """Starts the boss fight and prints the action.
        Method take 2 arguments.

        Argument:
        --------------
            char: obj
                player character
            boss: obj
                enemy character
        """
        while True:
            char.attack(boss)
            my_print(f'You are attacking with a power of {char.power}, '
                     f'your amor has {char.defence} '
                     f'durability and {char.hp} HP left\n')
            boss.attack(char)
            my_print(f'{boss.type_of} is attacking you with a power of {boss.power} and he has '
                     f'{boss.critical}% '
                     f'chance to deal double damage. {boss.type_of} '
                     f'armor has {boss.defence} points and '
                     f'{boss.hp} HP left\n')
            if boss.hp <= 0:
                my_print(f'Well done grand {char.type_of}!!! '
                         f'You defeated the terrifying {boss.type_of} and '
                         f'the realm is free!\n')
                break
            elif char.hp <= 0:
                my_print(f'''Our {char.type_of} has been killed 
                by the terrifying {boss.type_of} and the realm is destroyed!!! 
                         Rest in peace grand {char.type_of}\n''')
                break

    @staticmethod
    def fighting_scene(char):
        """Starts the fighting scene after the player choice of opening or not the chest
        Method takes 1 argument.

        Argument:
        --------------
            char: obj
                player character
        """
        clear_screen()
        Game.stop_sound()
        Game.play_sound_exploring()
        if Game.action():
            Game.player_open_chest(char)
            Game.main_battle(char)
        else:
            Game.player_no_chest(char)
            Game.main_battle(char)

    @staticmethod
    def main_battle(char):
        """Runs the battle in a loop, until one of the characters run out of hp
        This method withdraws a random enemy and takes 1 argument

        Argument:
        --------------
            char: obj
                player character
        """
        enemy = Game.chose_enemy()
        while True:
            Game.battle(enemy, char)
            if char.hp <= 0 or enemy.hp <= 0:
                break

    @staticmethod
    def increase_player_level(player, enemy):
        """Increase the player stats if he has enough xp, by getting data from json
         and overwrite it if level up. The players will have to chose what he wants to increase
         The method is running in a loop until the experience is depleted
         If player level is equal or bigger then 5 the boss fighting starts.
         Boss object is created.
         Method takes 2 arguments.
         Argument:
        --------------
            player: obj
                player character
            enemy: obj
                enemy character
         """
        player.experience += enemy.experience
        USER_PARAM['experience'] = player.experience
        save_data(USER_PARAM)
        while player.experience >= 100:
            player.level += 1
            USER_PARAM['level'] = player.level
            save_data(USER_PARAM)
            player.experience -= 100
            USER_PARAM['experience'] = player.experience
            save_data(USER_PARAM)
            clear_screen()
            my_print(f'''Congrats!!!
            You are now level {player.level}.
            Chose what do you want to increase:
            1. HP
            2. Defence
            3. Power\n''')
            user_input = my_input('''
            Please select 1, 2 or 3
            (if you press any other key, your power will be increased by default)\n''')
            clear_screen()
            if user_input == '1':
                player.hp += player.hp * 10 / 100
                USER_PARAM['hp'] = player.hp
                save_data(USER_PARAM)
                my_print(f"Your new life has {USER_PARAM.get('hp')} HP\n")
                clear_screen()
            elif user_input == '2':
                player.defence += player.defence * 10 / 100
                USER_PARAM['defence'] = player.defence
                save_data(USER_PARAM)
                my_print(f"Your new defence is {USER_PARAM.get('defence')}\n")
                clear_screen()
            else:
                player.power += player.power * 10 / 100
                USER_PARAM['power'] = player.power
                save_data(USER_PARAM)
                my_print(f"Your new power is {USER_PARAM.get('power')}\n")
                clear_screen()
        if player.level >= 5:
            Game.stop_sound()
            Game.play_sound_fight()
            my_print('Now you have to defeat the terrifying python '
                     'to save the realm once and for all\n!!!')
            clear_screen()
            boss = Python()
            Game.boss_fight(boss, player)

    @staticmethod
    def save_data_warrior(char):
        """Store the player data and stats in a json file and returns it
        Method takes on argument.
        Argument:
        --------------
            char: obj
                player character
        """
        USER_PARAM['name'] = char.name
        USER_PARAM['level'] = char.level
        USER_PARAM['experience'] = char.experience
        USER_PARAM['type_of'] = char.type_of
        USER_PARAM['hp'] = char.hp
        USER_PARAM['defence'] = char.defence
        USER_PARAM['power'] = char.power
        USER_PARAM['weapon'] = char.weapon
        USER_PARAM['armor'] = char.armor
        return save_data(USER_PARAM)
