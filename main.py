from Text_functions import *


TextFunction.intro_message()
user = input('Do you want to play? Press \'y\'for yes and \'n\' for exit the game\n')
if TextFunction.ask_if_play(user):
    user = input("""What character do you want to play:
                1. Wizard
                2. Warrior
                Please select 1 or 2.
                """)
    TextFunction.ask_type_of_char(user)
