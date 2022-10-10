from useful_function import *
from Enemy import *
from Player import *
import winsound

USER_PARAM = {
    'name': None,
    'experience': 0,
    'level': 1,
    'hp': 0,
    'defence': 0,
    'power': 0
}


class Start:

    @staticmethod
    def stop_sound():
        winsound.PlaySound(None, winsound.SND_PURGE)

    @staticmethod
    def play_sound_intro():
        winsound.PlaySound(r'C:\Users\ravva\PycharmProjects\Dungeon and Pythons\Music_Game\Main_Menu.wav',
                           winsound.SND_ASYNC + winsound.SND_LOOP)

    @staticmethod
    def play_sound_exploring():
        winsound.PlaySound(r'C:\Users\ravva\PycharmProjects\Dungeon and Pythons\Music_Game\Exploring.wav',
                           winsound.SND_ASYNC + winsound.SND_LOOP)

    @staticmethod
    def play_sound_fight():
        winsound.PlaySound(r'C:\Users\ravva\PycharmProjects\Dungeon and Pythons\Music_Game\BattleFinal.wav',
                           winsound.SND_ASYNC + winsound.SND_LOOP)

    @staticmethod
    def intro_message():
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
        user_answer = my_input("""Do you want to play again?
        Press \'y\' to play or press any key to leave the game\n""")
        clear_screen()
        if user_answer == 'y':
            Start.stop_sound()
            Start.play_sound_intro()
            return True
        else:
            my_print('''The realm needs you!!!
            Let's hope you will come back soon.''')
            return False

    @staticmethod
    def game():
        user_char = my_input(f"""What character do you want to play {USER_PARAM.get('name')}:
                            1. Wizard
                            2. Knight
        Please select 1 or 2 (If you press any another key, you will play as Knight by default).\n""")
        clear_screen()
        Start.ask_type_of_char(user_char)
        clear_screen()
        if user_char == '1':
            wizard = Wizard(USER_PARAM.get('name'))
            my_print(f'Thank you wizard {wizard.name} for choosing to protect us')
            Start.fighting_scene(wizard)
        else:
            knight = Knight(USER_PARAM.get('name'))
            my_print(f'Thank you Sir {knight.name} for choosing to protect us')
            Start.fighting_scene(knight)

    @staticmethod
    def game_intro():
        Start.play_sound_intro()
        Start.intro_message()
        user = my_input('''Do you want to play? 
        Press \'y\'to play or press any key exit the game\n''')
        clear_screen()
        if user == 'y':
            my_print("""Great!
            Let's fight for this realm!
        """)
            Start.ask_user_name()
            return True
        else:
            my_print('Hope you will come back soon.The land needs you')
            return False

    @staticmethod
    def ask_user_name():
        user = my_input('Please enter your name brave warrior: ')
        USER_PARAM['name'] = user
        clear_screen()

    @staticmethod
    def ask_type_of_char(user):
        if user == '1':
            Start.wizard_message()
        else:
            Start.knight_message()

    @staticmethod
    def choosing_path(user):
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
        user_path = my_input('''Now let's go to destroy our enemies.
                        You have arrived on a crossroad with 3 paths and you have to choose one!
                        1. To the forest
                        2. To the town
                        3. To the dungeon
        Please select 1, 2 or 3(if you press any other key, you will go to the dungeon by default \n''')
        clear_screen()
        Start.choosing_path(user_path)
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
        clear_screen()
        char.gear_up()
        my_print(f'Your power is {char.power} and your armor is {char.defence}\n')
        Start.stop_sound()
        Start.play_sound_fight()

    @staticmethod
    def player_open_chest(char):
        clear_screen()
        char.open_chest()
        my_print(f'You have found a {char.weapon_type} with power of {char.weapon} and a {char.armor_type} '
                 f'with extra defence of {char.armor}\n')
        char.gear_up()
        my_print(f'Your new power is {char.power} and your new armor is {char.defence}\n')
        Start.stop_sound()
        Start.play_sound_fight()

    @staticmethod
    def battle(enemy, char):
        char.attack(enemy)
        my_print(f'You are attacking with a power of {char.power}, your amor has {char.defence} '
                 f'durability and {char.hp} HP left\n')
        enemy.attack(char)
        my_print(f'{enemy.type_of} is attacking you with a power of {enemy.power} and he has '
                 f'{enemy.critical}% '
                 f'chance to deal double damage. {enemy.type_of} armor has {enemy.defence} points and '
                 f'{enemy.hp} HP left\n')
        if enemy.hp <= 0:
            my_print(f'Well done grand {char.type_of}!!! You defeated the {enemy.type_of}\n')
            Start.increase_player_level(char, enemy)
        elif char.hp <= 0:
            my_print(f'''Our {char.type_of} has been killed by a powerful {enemy.type_of}!!!
                            Rest in peace grand {char.type_of}\n''')
            return char.hp, enemy.hp

    @staticmethod
    def fighting_scene(char):
        clear_screen()
        Start.stop_sound()
        Start.play_sound_exploring()
        if Start.action():
            Start.player_open_chest(char)
            enemy = Start.chose_enemy()
            while True:
                Start.battle(enemy, char)
                if char.hp <= 0:
                    break
                elif enemy.hp <= 0:
                    break
        else:
            Start.player_no_chest(char)
            enemy = Start.chose_enemy()
            while True:
                Start.battle(enemy, char)
                if char.hp <= 0 or enemy.hp <= 0:
                    break

    @staticmethod
    def increase_player_level(player, enemy):
        player.experience += enemy.experience
        USER_PARAM['experience'] = player.experience
        while player.experience >= 100:
            player.level += 1
            USER_PARAM['level'] = player.level
            player.experience -= 100
            USER_PARAM['experience'] = player.experience
            my_print('''Chose what do you want to increase:
            1. HP
            2. Defence
            3. Power''')
            user_input = my_input(f'''Congrats!!!
            You are now level {player.level}.
            Please select 1, 2 or 3(if you press any other key, your power will be increased by default\n''')
            if user_input == '1':
                player.hp += player.hp * 10 / 100
                USER_PARAM['hp'] = player.hp
                my_print(f"Your new life has {USER_PARAM.get('hp')} HP")
            elif user_input == '2':
                player.defence += player.defence * 10 / 100
                USER_PARAM['defence'] = player.defence
                my_print(f"Your new defence is {USER_PARAM.get('defence')}")
            else:
                player.power += player.power * 10 / 100
                USER_PARAM['power'] = player.power
                my_print(f"Your new power is {USER_PARAM.get('power')}")
