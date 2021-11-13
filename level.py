from random import randint

def largest_index_position(lst1, lst2, lst3, lst4):
    indexes = [x for x in [max(lst1), max(lst2), max(lst3), max(lst4)]]
    return (max(indexes))

class level_map_gen:
    def __init__(self, int):
        self.size = randint(5, int)
        self.map = [['-' for x in range(0, self.size)] for x in range(0, self.size)]
    
    def print_map(self, lst_lst, hp, dmg):
        for i in lst_lst:
            print('  '.join(i))
        print(f'HP: {hp}   Dmg: {dmg}')
        print('% = stairs, # = enemy, * = loot')