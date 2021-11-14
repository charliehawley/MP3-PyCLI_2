import entity
import level
from random import randint

hero = entity.hero_init()

ent_dict = {'runt': ['runt', 3, 2], 'bruiser': ['bruiser', 4, 3], 'boss': ['boss', 10, 4], 'lunch': ['lunch', 0, 5], 'stimulant': ['stimulant', 0, 2], 'vigour': ['vigour', 0, 5]}

ent_names = list(ent_dict.keys())

l1 = [ent_dict['runt'], ent_dict[ent_names[randint(3, 5)]]]
l2 = [ent_dict['bruiser'], ent_dict[ent_names[randint(3, 5)]]]
l3 = [ent_dict['boss'], ent_dict[ent_names[randint(3, 5)]]]

enemy, loot, stairs = entity.ents_init(l1[0], l1[1])
# print(hero.position)
# print(enemy.position)
# print(loot.position)
# print(stairs.position)

map_limit = level.largest_index_position(hero.position, enemy.position, loot.position, stairs.position)
print(map_limit)
level_map = level.level_map_gen(map_limit)
hero_map_att = [hero.hp, hero.power, hero.icon, hero.position]
level_map.print_map(level_map.map, hero_map_att, enemy.position, loot.position, stairs.position)

other_ents_pos = [enemy.position, loot.position, stairs.position]

move = input('Where would you like to go...?\n')
check_pos = level_map.move_hero(hero_map_att, move, level_map.map, other_ents_pos, map_limit)
print(check_pos)
# level_map.print_map(level_map.map, hero_map_att, enemy.position, loot.position, stairs.position)
