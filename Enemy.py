import random


class Enemy:

    def __init__(self, type_of, hp, power, defence):
        self.type_of = type_of
        self.hp = hp
        self.power = power
        self.defence = defence
        self.experience = None
        self.critical = None

    def attack(self, user):
        if random.randint(1, 100) <= self.critical:
            if self.power <= user.defence:
                user.hp = user.hp
                user.defence -= 5
            else:
                user.hp -= (self.power - user.defence) * 2
                user.defence -= 5
        else:
            if self.power <= user.defence:
                user.hp = user.hp
                user.defence -= 5
            else:
                user.hp -= self.power - user.defence
                user.defence -= 5


class Goblin(Enemy):

    def __init__(self, type_of='Goblin', hp=800, power=120, defence=80):
        super().__init__(type_of, hp, power, defence)
        self.critical = 10
        self.experience = 50


class Orc(Enemy):

    def __init__(self, type_of='Orc', hp=900, power=140, defence=90):
        super().__init__(type_of, hp, power, defence)
        self.critical = 25
        self.experience = 100


class Troll(Enemy):

    def __init__(self, type_of='Troll', hp=1100, power=180, defence=100):
        super().__init__(type_of, hp, power, defence)
        self.critical = 35
        self.experience = 150
