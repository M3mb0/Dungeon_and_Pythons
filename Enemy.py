import random


class Enemy:

    def __init__(self, type_of, hp, power, defence):
        self.type_of = type_of
        self.hp = hp
        self.power = power
        self.defence = defence
        self.critical = None

    def attack(self, user):
        if random.randint(1, 100) <= self.critical:
            user.hp -= (self.power - user.defence) * 2
            user.defence -= 5
        else:
            user.hp -= self.power - user.defence
            user.defence -= 5


class Goblin(Enemy):

    def __init__(self, type_of='Goblin', hp=500, power=70, defence=10):
        super().__init__(type_of, hp, power, defence)
        self.critical = 10


class Orc(Enemy):

    def __init__(self, type_of='Orc', hp=800, power=100, defence=50):
        super().__init__(type_of, hp, power, defence)
        self.critical = 20


class Troll(Enemy):

    def __init__(self, type_of='Troll', hp=1200, power=200, defence=100):
        super().__init__(type_of, hp, power, defence)
        self.critical = 50
