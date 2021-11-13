from random import randint

def largest_index_position(lst1, lst2, lst3, lst4):
    indexes = [x for x in [max(lst1), max(lst2), max(lst3), max(lst4)]]
    return (max(indexes))

class level_map_gen:
    def __init__(self, int):
        self.map = [['-' for x in range(0, int + 1)] for x in range(0, int + 1)]
    
    def print_map(self, lst_lst, hp, dmg, hero_pos, enemy_pos, loot_pos, stairs_pos, hero_name ):
        lst_lst[hero_pos[0]][hero_pos[1]] = hero_name[0]
        lst_lst[enemy_pos[0]][enemy_pos[1]] = '#'
        lst_lst[loot_pos[1]][loot_pos[0]] = '?'
        lst_lst[stairs_pos[0]][stairs_pos[1]] = '/'
        for i in lst_lst:
            print('  '.join(i))
        print(f'HP: {hp}   Dmg: {dmg}')
        print('# = enemy, ? = loot, / = stairs')