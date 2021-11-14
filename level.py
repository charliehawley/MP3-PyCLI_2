import os
from random import randint

def check_hero_pos(lst_lst, hero_next_pos):
    print(hero_next_pos)
    if lst_lst[hero_next_pos[0]][hero_next_pos[1]] == '/':
        return 'stairs' #will return 'stairs' which will load next level
    elif lst_lst[hero_next_pos[0]][hero_next_pos[1]] == '?':
        return 'loot' #will return 'loot' which will trigger loot.name's effect
    elif lst_lst[hero_next_pos[0]][hero_next_pos[1]] == '#':
        return 'fight' #will return 'enemy' which will trigger e.hp - h.pow, h.hp - e.pow until either hp is depleted
    else:
        return 'walk'

def largest_index_position(lst1, lst2, lst3, lst4):
    indexes = [x for x in [max(lst1), max(lst2), max(lst3), max(lst4)]]
    return (max(indexes))

class level_map_gen:
    def __init__(self, int):
        self.map = [['-' for x in range(0, int + 1)] for x in range(0, int + 1)]
    
    def print_map(self, lst_lst, hero_lst, enemy_pos, loot_pos, stairs_pos):
        lst_lst[enemy_pos[0]][enemy_pos[1]] = '#'
        lst_lst[loot_pos[0]][loot_pos[1]] = '?'
        lst_lst[stairs_pos[0]][stairs_pos[1]] = '/'
        lst_lst[hero_lst[3][0]][hero_lst[3][1]] = hero_lst[2]
        for i in lst_lst:
            print('  '.join(i))
        print(f'HP: {hero_lst[0]}   Dmg: {hero_lst[1]}')
        print('# = enemy, ? = loot, / = stairs')

    def move_hero(self, hero_lst, dir, lst_lst, map_limit):
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
