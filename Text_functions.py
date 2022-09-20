import os
import sys
import time
import winsound


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
    os.system('cls')


class TextFunction:

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
            TextFunction.ask_type_of_char(user)
            return True
        elif user == 'n':
            my_print('Hope you will come back soon.The land needs you')
            return False

    @staticmethod
    def ask_type_of_char(user):
        if user == '1':
            TextFunction.wizard_message()
        elif user == '2':
            TextFunction.warrior_message()

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
            This town is no ruled by some scary creatures and all humans were kill by them.
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
