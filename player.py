"""Player character creator by using classes.

This script allows the user to create 2 warrior objects for fighting the enemies
and contain the fallowing:

Classes:
    --------------
    Player:
        the parent class which contain the methods applied to the children classes
        and takes 6 arguments
    Wizard:
        1st child class inherited from Player class
    Knight:
        2nd child class inherited from Player class

Methods:
    --------------
    attack:
        script used for attacking the enemy
    gear_up:
        script used to equip the player character
    open_chest:
        script used to open chests with items for the character

Other imports:
    --------------
    random:
        module used in open_chest method to create random values for found items
"""

import random


class Player:
    """Class Player is a parent class, gets 6 attributes and has 3 methods
    which are used in children classes.

Attributes:
    --------------
    name: str
        The name of the player
    hp: int
        The hit points of the character
    power: int
        The hitting power of the character
    defence: int
        The amount of damage witch can be blocked
    weapon: int
        The hitting power of the weapon
    armor: int
        The amount of damage that can be blocked by the armor

Method:
    --------------
    attack:
        is taking 1 argument and is used to set up the new stats for the enemy
        after the player's attack
    gear_up:
        is used to set up the new stats of the player character
    open_chest:
        is used to open the chest and getting new items
"""

    def __init__(self, name, hp, power, defence, weapon, armor):
        self.name = name
        self.hp = hp
        self.power = power
        self.defence = defence
        self.weapon = weapon
        self.armor = armor

    def attack(self, user):
        """"Method is taking one argument and is used to set up the new stats (class attributes)
        of the enemy after the attack.

        Attack method use the power attribute to deal damage to the enemy.

        Argument:
        --------------
        user: obj
            An object that describe an enemy to be attacked
        """
        if self.power <= user.defence:
            user.hp = user.hp
            user.defence -= 5
        else:
            user.hp -= self.power - user.defence
            user.defence -= 5

    def gear_up(self):
        """Method does not take arguments and is used to enhance the player attributes.

        Attributes that are enhanced:
        --------------
        power: int
            standard power value is added with the power of the weapon
        defence: int
            standard defence value is added with the of the armor
        """
        self.power += self.weapon
        self.defence += self.armor

    def open_chest(self):
        """Method does not take arguments and is used to change the
        player attributes after is the chest is opened

        Attributes that are changed:
        --------------
        weapon: int
            weapon value is changed by using random module
        armor: int
            armor value is changed by using random module
        """
        self.weapon = random.randrange(100, 500, 50)
        self.armor = random.randrange(10, 100, 10)


class Wizard(Player):
    """Class Wizard is a child class inherited from Player class and gets 5 extra attributes.
    The parent class ( Player) attributes are already set up except the name attribute

    Attributes:
        --------------
        name: str
            The name of the player -> needs to be set
        hp: int
            The hit points of the character -> already set
        power: int
            The hitting power of the character -> already set
        defence: int
            The amount of damage who can be blocked -> already set
        weapon: int
            The hitting power of the weapon -> already set
        armor: int
            The amount of damage that can be blocked by the armor -> already set
        weapon_type: str
            The type of the weapon -> already set
        armor_type: str
            The type of the armor -> already set
        type_of: str
            The type of the character -> already set
        experience: int
            Set by default to 0 -> already set
        level: int
            Set by default to 1 -> already set
    """

    def __init__(self, name, hp=500, power=150, defence=30, weapon=200, armor=20):
        super().__init__(name, hp, power, defence, weapon, armor)
        self.weapon_type = 'wand'
        self.armor_type = 'robe'
        self.type_of = 'wizard'
        self.experience = 0
        self.level = 1


class Knight(Player):
    """Class Knight is a child class inherited from Player class and gets 5 extra attributes.
        The parent class ( Player) attributes are already set up except the name attribute

        Attributes:
            --------------
            name: str
                The name of the player -> needs to be set
            hp: int
                The hit points of the character -> already set
            power: int
                The hitting power of the character -> already set
            defence: int
                The amount of damage who can be blocked -> already set
            weapon: int
                The hitting power of the weapon -> already set
            armor: int
                The amount of damage that can be blocked by the armor -> already set
            weapon_type: str
                The type of the weapon -> already set
            armor_type: str
                The type of the armor -> already set
            type_of: str
                The type of the character -> already set
            experience: int
                Set by default to 0 -> already set
            level: int
                Set by default to 1 -> already set
        """

    def __init__(self, name, hp=800, power=60, defence=60, weapon=100, armor=40):
        super().__init__(name, hp, power, defence, weapon, armor)
        self.weapon_type = 'sword'
        self.armor_type = 'armor'
        self.type_of = 'knight'
        self.experience = 0
        self.level = 1
