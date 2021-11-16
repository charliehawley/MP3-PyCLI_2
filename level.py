"""Level Module:
This module handles the UI for Gone Rouge,
generating and printing maps to the CLI,
initialising entities, spawning entity sprites
and moving the hero sprite.

Functions:
    - LevelMapGen (__init__)
    - largest index position
    - print_map
    - check_hero_pos
    - move_hero"""
import os


class LevelMapGen:
    """
    Creates an instance of the level

        ARGS: integer representing maximum map size

        RETURNS: object - list as 'map' to be iterated through
                 and printed on screen
    """
    def __init__(self, num):
        self.map = [['-' for x in range(0, num + 1)]
                    for x in range(0, num + 1)]


def largest_index_position(lst1, lst2, lst3, lst4):
    """
    Defines max map size by taking the largest integer from a list of indexes

        ARGS: randomly generated index positions (lists) for all entities

        RETURNS: integer representing the maximum map size
                 for generating the level map
    """
    indexes = [max(lst1), max(lst2), max(lst3), max(lst4)]
    return max(indexes)


def print_map(lst_lst, hero_lst, enemy_pos, loot_pos, stairs_pos,
              gone_rogue_logo):
    """
    Prints level to terminal using a list generated with LevelMapGen.map

        ARGS: lists - level map, (hero.h_p, hero.power, hero.icon,
              hero.position), enemy.position, loot.position, stairs.position,
              GONE_ROGUE_LOGO

        RETURNS: updates level map list and prints level map
    """
    # clears screen
    os.system('cls' if os.name == 'nt' else 'clear')
    # prints title
    print(gone_rogue_logo)
    print("Welcome to Gone Rogue\n")
    # print(level_name)
    # prints map list using iteration replacing empty spaces
    # with entity sprites
    lst_lst[enemy_pos[0]][enemy_pos[1]] = '#'
    lst_lst[loot_pos[0]][loot_pos[1]] = '?'
    lst_lst[stairs_pos[0]][stairs_pos[1]] = '/'
    lst_lst[hero_lst[3][0]][hero_lst[3][1]] = hero_lst[2]
    for i in lst_lst:
        print('  '.join(i))
    # prints hp, damage and level map index
    print(f'HP: {hero_lst[0]}   Dmg: {hero_lst[1]}')
    print('# = enemy, ? = loot, / = stairs')


def check_hero_pos(lst_lst, hero_next_pos):
    """
    Checks for entity in position index requested by move_hero()

        ARGS: level map list, requested positional index for hero sprite

        RETURNS: string to be used to trigger encounters
    """
    print(hero_next_pos)
    if lst_lst[hero_next_pos[0]][hero_next_pos[1]] == '/':
        return 'stairs'
    if lst_lst[hero_next_pos[0]][hero_next_pos[1]] == '?':
        return 'loot'
    if lst_lst[hero_next_pos[0]][hero_next_pos[1]] == '#':
        return 'fight'
    else:
        return 'walk'


def move_hero(hero_lst, wasd, lst_lst, map_limit):
    """
    Changes hero position index based on user input

        ARGS: list - (hero.h_p, hero.power, hero.icon, hero.position),
              string - direction, level_map.map

        RETURNS: string - result of check_hero_pos, updated hero.position
    """
    if wasd == 'w':
        if (hero_lst[3][0] - 1) < 0:
            return ['oob', hero_lst[3]]
        else:
            lst_lst[hero_lst[3][0]][hero_lst[3][1]] = '-'
            hero_lst[3][0] -= 1
            check_pos = check_hero_pos(lst_lst, hero_lst[3])
            lst_lst[hero_lst[3][0]][hero_lst[3][1]] = hero_lst[2]
            os.system('cls' if os.name == 'nt' else 'clear')
            return [check_pos, hero_lst[3]]
    elif wasd == 's':
        if (hero_lst[3][0] + 1) > map_limit:
            return ['oob', hero_lst[3]]
        else:
            lst_lst[hero_lst[3][0]][hero_lst[3][1]] = '-'
            hero_lst[3][0] += 1
            check_pos = check_hero_pos(lst_lst, hero_lst[3])
            lst_lst[hero_lst[3][0]][hero_lst[3][1]] = hero_lst[2]
            os.system('cls' if os.name == 'nt' else 'clear')
            return [check_pos, hero_lst[3]]
    elif wasd == 'a':
        if (hero_lst[3][1] - 1) < 0:
            return ['oob', hero_lst[3]]
        else:
            lst_lst[hero_lst[3][0]][hero_lst[3][1]] = '-'
            hero_lst[3][1] -= 1
            check_pos = check_hero_pos(lst_lst, hero_lst[3])
            lst_lst[hero_lst[3][0]][hero_lst[3][1]] = hero_lst[2]
            os.system('cls' if os.name == 'nt' else 'clear')
            return [check_pos, hero_lst[3]]
    elif wasd == 'd':
        if (hero_lst[3][1] + 1) > map_limit:
            return ['oob', hero_lst[3]]
        else:
            lst_lst[hero_lst[3][0]][hero_lst[3][1]] = '-'
            hero_lst[3][1] += 1
            check_pos = check_hero_pos(lst_lst, hero_lst[3])
            lst_lst[hero_lst[3][0]][hero_lst[3][1]] = hero_lst[2]
            os.system('cls' if os.name == 'nt' else 'clear')
            return [check_pos, hero_lst[3]]
    else:
        return [None, hero_lst[3]]
