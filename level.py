"""Level Module: 
This module handles the UI for Gone Rouge.

The LevelMapGen class generates a list to be printed 
as the level map in the CLI.


"""
import os


def check_hero_pos(lst_lst, hero_next_pos):
    """
    Checks for entity in position requested for hero by user
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


def largest_index_position(lst1, lst2, lst3, lst4):
    """
    Takes indexe positions for all entities and returns an integer
    representing the maximum map size for rendering the level
    """
    indexes = [max(lst1), max(lst2), max(lst3), max(lst4)]
    return max(indexes)


class LevelMapGen:
    """
    Creates an instance of the level
    and stores 'map' as list to be iterated through
    and printed on screen
    """
    def __init__(self, num):
        self.map = [['-' for x in range(0, num + 1)]
                    for x in range(0, num + 1)]

    def print_map(self, lst_lst, hero_lst, enemy_pos, loot_pos, stairs_pos,
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

    def move_hero(self, hero_lst, dir, lst_lst, map_limit):
        """
        Changes hero posiiton index based on user input
        """
        if dir == 'w':
            if (hero_lst[3][0] - 1) < 0:
                return ['oob', hero_lst[3]]
            else:
                lst_lst[hero_lst[3][0]][hero_lst[3][1]] = '-'
                hero_lst[3][0] -= 1
                check_pos = check_hero_pos(lst_lst, hero_lst[3])
                lst_lst[hero_lst[3][0]][hero_lst[3][1]] = hero_lst[2]
                os.system('cls' if os.name == 'nt' else 'clear')
                return [check_pos, hero_lst[3]]
        elif dir == 's':
            if (hero_lst[3][0] + 1) > map_limit:
                return ['oob', hero_lst[3]]
            else:
                lst_lst[hero_lst[3][0]][hero_lst[3][1]] = '-'
                hero_lst[3][0] += 1
                check_pos = check_hero_pos(lst_lst, hero_lst[3])
                lst_lst[hero_lst[3][0]][hero_lst[3][1]] = hero_lst[2]
                os.system('cls' if os.name == 'nt' else 'clear')
                return [check_pos, hero_lst[3]]
        elif dir == 'a':
            if (hero_lst[3][1] - 1) < 0:
                return ['oob', hero_lst[3]]
            else:
                lst_lst[hero_lst[3][0]][hero_lst[3][1]] = '-'
                hero_lst[3][1] -= 1
                check_pos = check_hero_pos(lst_lst, hero_lst[3])
                lst_lst[hero_lst[3][0]][hero_lst[3][1]] = hero_lst[2]
                os.system('cls' if os.name == 'nt' else 'clear')
                return [check_pos, hero_lst[3]]
        elif dir == 'd':
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
