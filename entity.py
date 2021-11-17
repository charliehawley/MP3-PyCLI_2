"""Entity Module:
This module handles the generation of entities
and their attributes in Gone Rogue

Functions:
    - Ent (__init__)
    - hero_init
    - ents_init"""
from random import randint

hero_position = [(randint(0, 6)), (randint(0, 6))]


class Ent:
    """
    Creates an instance of entity

        ARGS: string - name, ints - hp, power, list - position

        RETURNS: entity object
    """
    def __init__(self, name, h_p, power, position):
        self.name = name
        self.h_p = h_p
        self.power = power
        self.icon = name[0]
        self.position = position


def hero_init():
    """
    Initialises hero using Ent class and validates user input

        ARGS: user input assigned to h_name

        RETURNS: hero object
    """
    while True:
        try:
            h_name = input('\nWhat is your name hero?\n')
            # establishes whether hero name starts with alpha character
            # (hero icon must be alpha
            # to determine reliably against other entities (non-alpha))
            if h_name[0].isalpha():
                # uses Ent __init__ to initialise hero
                hero = Ent(h_name, 15, 3, hero_position)
                return hero
            else:
                print("""
    That's an unusual name,
    would you mind anglicizing it...""")
        except IndexError:
            print('But you must have a name?')


def ents_init(enemy_ent, loot_ent):
    """
    Initialises enemy, loot and stairs entities
    using Ent class and ensures exclusive positional indexes

        ARGS: lists - positional indexes for enemy and loot

        RETURNS: enemy object, loot object, stairs object
    """
    enemy_position = [(randint(0, 6)), (randint(0, 6))]
    loot_position = [(randint(0, 6)), (randint(0, 6))]
    stairs_position = [(randint(0, 6)), (randint(0, 6))]

    a = hero_position
    b = enemy_position
    c = loot_position
    d = stairs_position

    # resets enemy_position if it matches hero_position
    while a == b:
        enemy_position = [(randint(0, 6)), (randint(0, 6))]
    # initialises enemy
    enemy_ent = Ent(enemy_ent[0], enemy_ent[1], enemy_ent[2], enemy_position)

    # resets loot position if it matches either hero_position or enemy_position
    while c in (a, b):
        loot_position = [(randint(0, 6)), (randint(0, 6))]
    # initialises loot
    loot_ent = Ent(loot_ent[0], loot_ent[1], loot_ent[2], loot_position)

    # resets stairs position if it matches either hero_position, enemy_position
    # or loot_position
    while d in (a, b, c):
        stairs_position = [(randint(0, 6)), (randint(0, 6))]
    # initialises stairs
    stairs_ent = Ent('stairs', 0, 0, stairs_position)

    return enemy_ent, loot_ent, stairs_ent
