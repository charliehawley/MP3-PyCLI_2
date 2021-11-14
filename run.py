import entity
import level
from random import randint

hero = entity.hero_init()

ent_dict = {'runt': ['runt', 10, 2], 'bruiser': ['bruiser', 4, 3], 'boss': ['boss', 10, 4], 'lunch': ['lunch', 0, 5], 'stimulant': ['stimulant', 0, 2], 'vigour': ['vigour', 0, 5]}

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

hero_map_att[3] = check_pos[1]
level_map.print_map(level_map.map, hero_map_att, enemy.position, loot.position, stairs.position)

def battle():
        enemy.hp -= hero.power
        print(f'{hero.name} hits {enemy.name}. {enemy.name} hp: {enemy.hp}')
        if hero.hp < 0:
            print("That's GAME OVER pal!")
        elif hero.hp > 0 and enemy.hp <= 0:
            print(f'You defeated {enemy.name}!')
        else:
            hero.hp -= enemy.power
            print(f'{enemy.name} hits {hero.name}. {hero.name} hp: {hero.hp}')
            if hero.hp < 0:
                print("That's GAME OVER pal!")
            elif hero.hp > 0 and enemy.hp < 0:
                print(f'You defeated {enemy.name}!')
            else:
                pass

while True:
    if check_pos[0] == 'walk':
        move = input('Where would you like to go...?\n')
        check_pos = level_map.move_hero(hero_map_att, move, level_map.map, other_ents_pos, map_limit)
        hero_map_att[3] = check_pos[1]
        level_map.print_map(level_map.map, hero_map_att, enemy.position, loot.position, stairs.position)
        continue
    elif check_pos[0] == 'loot':
        print(f'You picked up {loot.name[1:]}!')
        if loot.name == 'lunch':
            hero.hp += lunch.power
            print("It's delicious...")
            print(f'You gained {lunch.power} hp.')
        elif loot.name == 'stimulant':
            hero.power *= stimulant.power
            print('You feel way juiced, man!')
            print('Your bloodied fists twitch, itching to get to work.')
        else:
            hero.power += loot.power
            print("Is that ginger and chilli?")
            print('WOW that packs a punch!')
        check_pos[0] = 'walk'
        continue
    elif check_pos[0] == 'fight':
        battle()
        check_pos[0] = 'walk'
    else:
        print('Going up?')
        break




    



# level_map.print_map(level_map.map, hero_map_att, enemy.position, loot.position, stairs.position)
