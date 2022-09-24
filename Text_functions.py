from useful_function import *
from Enemy import *
import winsound


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
    def warrior_message():
        my_print("""Congratulations, great warrior!
          ->  Warriors were
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
    def ask_if_play(user):
        if user == 'y':
            my_print("""Great!
            Let's fight for this realm!
        """)
            Start.ask_type_of_char(user)
            return True
        elif user == 'n':
            my_print('Hope you will come back soon.The land needs you')
            return False

    @staticmethod
    def ask_type_of_char(user):
        if user == '1':
            Start.wizard_message()
        elif user == '2':
            Start.warrior_message()

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
        elif user == '3':
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
                        Please select 1, 2 or 3\n''')
        clear_screen()
        Start.choosing_path(user_path)
        clear_screen()
        if my_input('''You have found a chest!
                You can choose to open it and getting a better or worse weapon and armor
                or you can leave it and fight using your own items.
                What it will be?
                Do you risk or not?
                Type -y- to risk or -n- to keep your items\n''') == 'y':
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
