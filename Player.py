import random
import math

class Player:

    def __init__(self, name, hp, power, defence, weapon, armor):
        self.hp = hp
        self.name = name
        self.power = power
        self.defence = defence
        self.weapon = weapon
        self.armor = armor

    def attack(self, user):
        if self.power <= user.defence:
            user.hp = user.hp
        else:
            user.hp -= self.power - user.defence
            user.defence -= 5

    def gear_up(self):
        self.power += self.weapon
        self.defence += self.armor

    def open_chest(self):
        self.weapon = random.randrange(100, 500, 50)
        self.armor = random.randrange(10, 100, 10)


class Wizard(Player):

    def __init__(self, name, hp=500, power=120, defence=30, weapon=100, armor=20):
        super().__init__(name, hp, power, defence, weapon, armor)


class Warrior(Player):

    def __init__(self, name, hp=800, power=60, defence=60, weapon=100, armor=20):
        super().__init__(name, hp, power, defence, weapon, armor)
