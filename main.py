"""Main script to start playing the game"""

from game_functionality import Game


if Game.game_intro():
    while Game.play_again():
        Game.continue_fighting()
