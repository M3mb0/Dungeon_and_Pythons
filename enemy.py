"""Enemy character creator by using classes.

This script allows the user to create 4 enemy objects for fighting the players
and contain the fallowing:

Classes:
    --------------
    Enemy:
        the parent class which contain the methods applied to the children classes
        and takes 6 arguments
    Goblin:
        1st child class inherited from Enemy class
    Orc:
        2nd child class inherited from Enemy class
    Troll:
        3rd child class inherited from Enemy class
    Python:
        4th child class inherited from Enemy class

Methods:
    --------------
    attack:
        script used for attacking the player

Other imports:
    --------------
    random:
        module used in open_chest method to create random values for found items
"""

import random


class Enemy:
    """Class Enemy is a parent class, gets 6 attributes and has 1 method
        which is used in children classes.

    Attributes:
        --------------
        type_of: str
            The type of the enemy
        hp: int
            The hit points of the character
        power: int
            The hitting power of the character
        defence: int
            The amount of damage which can be blocked
        experience: None
            The experience offered by the enemy if is killed
        critical: None
            The chance that the enemy has to deal critical damage

    Method:
        --------------
        attack:
            is taking 1 argument and is used to set up the new stats for the player
            after the enemy's attack
    """

    def __init__(self, type_of, hp, power, defence):
        self.type_of = type_of
        self.hp = hp
        self.power = power
        self.defence = defence
        self.experience = None
        self.critical = None

    def attack(self, user):
        """"Method is taking one argument and is used to set up the new stats (class attributes)
        of the player after the attack.

        Attack method use the power attribute to deal damage to the player.

        Argument:
        --------------
        user: obj
            An object that describe a player to be attacked
        """
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
    """Class Goblin is a child class inherited from Enemy class and gets 6 attributes.
        The parent class (Enemy) attributes are already set up.
        Goblin is the weakest of all enemies

        Attributes:
            --------------
            type_of: str
                The type of the enemy -> already set
            hp: int
                The hit points of the character -> already set
            power: int
                The hitting power of the character -> already set
            defence: int
                The amount of damage who can be blocked -> already set
            critical: int
                The chance that the enemy has to deal critical damage -> already set
            experience: int
                The experience offered by the enemy if is killed -> already set
        """

    def __init__(self, type_of='Goblin', hp=800, power=120, defence=80):
        super().__init__(type_of, hp, power, defence)
        self.critical = 10
        self.experience = 50


class Orc(Enemy):
    """Class Orc is a child class inherited from Enemy class and gets 6 attributes.
        The parent class (Enemy) attributes are already set up and
        Orc is the 2nd in terms of power, hp, defence and critical chance

        Attributes:
            --------------
            type_of: str
                The type of the enemy -> already set
            hp: int
                The hit points of the character -> already set
            power: int
                The hitting power of the character -> already set
            defence: int
                The amount of damage who can be blocked -> already set
            critical: int
                The chance that the enemy has to deal critical damage -> already set
            experience: int
                The experience offered by the enemy if is killed -> already set
        """

    def __init__(self, type_of='Orc', hp=900, power=140, defence=90):
        super().__init__(type_of, hp, power, defence)
        self.critical = 25
        self.experience = 100


class Troll(Enemy):
    """Class Goblin is a child class inherited from Enemy class and gets 6 attributes.
           The parent class (Enemy) attributes are already set up
           Troll is the 1st in terms of power, hp, defence and critical chance

           Attributes:
               --------------
               type_of: str
                   The type of the enemy -> already set
               hp: int
                   The hit points of the character -> already set
               power: int
                   The hitting power of the character -> already set
               defence: int
                   The amount of damage who can be blocked -> already set
               critical: int
                   The chance that the enemy has to deal critical damage -> already set
               experience: int
                   The experience offered by the enemy if is killed -> already set
           """

    def __init__(self, type_of='Troll', hp=1100, power=180, defence=100):
        super().__init__(type_of, hp, power, defence)
        self.critical = 35
        self.experience = 150


class Python(Enemy):
    """Class Goblin is a child class inherited from Enemy class and gets 5 attributes.
           The parent class (Enemy) attributes are already set up
           Python is the boss enemy and cannot be attacked until player reach lvl 6

           Attributes:
               --------------
               type_of: str
                   The type of the enemy -> already set
               hp: int
                   The hit points of the character -> already set
               power: int
                   The hitting power of the character -> already set
               defence: int
                   The amount of damage who can be blocked -> already set
               critical: int
                   The chance that the enemy has to deal critical damage -> already set
           """

    def __init__(self, type_of='Python', hp=4400, power=600, defence=250):
        super().__init__(type_of, hp, power, defence)
        self.critical = 50
