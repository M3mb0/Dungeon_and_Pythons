class Enemy:

    def __init__(self, hp, power, armor):
        self.hp = hp
        self.power = power
        self.armor = armor

    def attack(self, user):
        user.hp -= self.power - user.armor


class Goblin(Enemy):

    def __init__(self, hp=50, power=50, armor=10):
        super().__init__(hp, power, armor)


class Orc(Enemy):

    def __init__(self, hp=70, power=70, armor=50):
        super().__init__(hp, power, armor)


class Troll(Enemy):

    def __init__(self, hp=100, power=100, armor=100):
        super().__init__(hp, power, armor)
