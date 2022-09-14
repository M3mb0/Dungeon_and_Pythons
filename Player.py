class Player:

    def __init__(self, name, hp, power, armor):
        self.hp = hp
        self.name = name
        self.power = power
        self.armor = armor
        self.inventory = []

    def attack(self, user):
        user.hp -= self.power - user.armor


class Wizard(Player):

    def __init__(self, name, hp=50, power=120, armor=10):
        super().__init__(name, hp, power, armor)


class Warrior(Player):

    def __init__(self, name, hp=120, power=50, armor=50):
        super().__init__(name, hp, power, armor)
