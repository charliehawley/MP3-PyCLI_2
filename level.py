"""Level Module: 
This module handles the UI for Gone Rouge,
generating and printing maps to the CLI,
initialising entities, spawning entity sprites 
and moving the hero sprite.

Functions:
- check_hero_pos: checks for entity encounter
- largest index position


"""
import os


class LevelMapGen:
    """
    Creates an instance of the level
    and stores 'map' as list to be iterated through
    and printed on screen
    """
    def __init__(self, num):
        self.map = [['-' for x in range(0, num + 1)]
                    for x in range(0, num + 1)]


def largest_index_position(lst1, lst2, lst3, lst4):
    """
    Takes index positions for all entities and returns an integer
    representing the maximum map size for rendering the level
    """
    indexes = [max(lst1), max(lst2), max(lst3), max(lst4)]
    return max(indexes)


def print_map(lst_lst, hero_lst, enemy_pos, loot_pos, stairs_pos,
              gone_rogue_logo):
    """
    Prints level to terminal using a list generated with self.map
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(gone_rogue_logo)
    print("Welcome to Gone Rogue\n")
    # print level name
    lst_lst[enemy_pos[0]][enemy_pos[1]] = '#'
    lst_lst[loot_pos[0]][loot_pos[1]] = '?'
    lst_lst[stairs_pos[0]][stairs_pos[1]] = '/'
    lst_lst[hero_lst[3][0]][hero_lst[3][1]] = hero_lst[2]
    for i in lst_lst:
        print('  '.join(i))
    print(f'HP: {hero_lst[0]}   Dmg: {hero_lst[1]}')
    print('# = enemy, ? = loot, / = stairs')


def check_hero_pos(lst_lst, hero_next_pos):
    """
    Checks for entity in position index requested by move_hero()
    returns string to be used to trigger encounters
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
    Changes hero posiiton index based on user input
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
