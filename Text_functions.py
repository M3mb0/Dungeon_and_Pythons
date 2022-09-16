from playsound import playsound


class TextFunction:

    @staticmethod
    def intro_message():
        playsound(r'C:\Users\ravva\PycharmProjects\Dungeon and Pythons\Music_Game\Main_Menu.wav', False)
        print("""Welcome stranger.
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
        playsound(r'C:\Users\ravva\PycharmProjects\Dungeon and Pythons\Music_Game\Main_Menu.wav', False)
        print("""Congratulations, grand wizard!
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
        playsound(r'C:\Users\ravva\PycharmProjects\Dungeon and Pythons\Music_Game\Main_Menu.wav', False)
        print("""Congratulations, great warrior!
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
            print("""Great!
            Let's fight for this realm!
        """)
        elif user == 'n':
            print('Hope you will come back soon.The land needs you')
