import os
import sys
from random import randint
import entity
import level

gone_rogue_logo = """
  ▄████  ▒█████   ███▄    █ ▓█████     ██▀███   ▒█████    ▄████  █    ██ ▓█████
 ██▒ ▀█▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀    ▓██ ▒ ██▒▒██▒  ██▒ ██▒ ▀█▒ ██  ▓██▒▓█   ▀
▒██░▄▄▄░▒██░  ██▒▓██  ▀█ ██▒▒███      ▓██ ░▄█ ▒▒██░  ██▒▒██░▄▄▄░▓██  ▒██░▒███
░▓█  ██▓▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄    ▒██▀▀█▄  ▒██   ██░░▓█  ██▓▓▓█  ░██░▒▓█  ▄
░▒▓███▀▒░ ████▓▒░▒██░   ▓██░░▒████▒   ░██▓ ▒██▒░ ████▓▒░░▒▓███▀▒▒▒█████▓ ░▒████
 ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░  ░▒   ▒ ░▒▓▒ ▒ ▒ ░░ ▒░
  ░   ░   ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░     ░▒ ░ ▒░  ░ ▒ ▒░   ░   ░ ░░▒░ ░ ░  ░ ░
░ ░   ░ ░ ░ ░ ▒     ░   ░ ░    ░        ░░   ░ ░ ░ ░ ▒  ░ ░   ░  ░░░ ░ ░    ░
      ░     ░ ░           ░    ░  ░      ░         ░ ░        ░    ░        ░
      """


def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(gone_rogue_logo)
    print("Welcome to Gone Rogue")
    while True:
        menu_choice = input('\ni = intro, c = controls, s = start\n')
        if menu_choice == 'i':
            print("\033[A                             \033[A")
            print("\033[A                             \033[A")
            print("\033[A                             \033[A\n")
            print("""
At the dawn of the 1980s, rudimentary programming made a small step
into the world of procedural generation in gaming.
Two men Michael Toy and Glenn Wichman
    PRESS ENTER""")
            input()
            print("\033[A                             \033[A")
            print("\033[A                             \033[A")
            print("They disappeared...\n    PRESS ENTER")
            input()
            print("\033[A                             \033[A")
            print("\033[A                             \033[A")
            print("Years later, the world realised...\n    PRESS ENTER")
            input()
            print("\033[A                             \033[A")
            print("\033[A                             \033[A")
            print("...they'd GONE ROGUE'\n    PRESS ENTER")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
            print(gone_rogue_logo)
            print("Welcome to Gone Rogue")
        elif menu_choice == 'c':
            print("\033[A                             \033[A")
            print("\033[A                             \033[A")
            print("\033[A                                      \033[A")
            print("""
The world of Gone Rogue is unique every time you play.
Once you enter the game, randomness dictates your experience.
Many parameters of the game like map size,
loot attributes, and spawn positions are randomised.

To navigate through the world you must input a direction and press enter.

w = ^
a = <
s = v
d = >

You'll want to grab any loot available (?) before beginning encounters.
Loot has randomised effects. You could find a nutritious lunch,
or end up making sacrifices for your blood sport.

Enemy (#) encounters are triggered by walking over them.
Once you step into an encounter there's no going back,
in the world of Gone Rogue, it's always a fight to the death.""")
            input('     PRESS ENTER...')
            os.system('cls' if os.name == 'nt' else 'clear')
            print(gone_rogue_logo)
            print("Welcome to Gone Rogue")

        elif menu_choice == 's':
            print('It begins...')
            os.system('cls' if os.name == 'nt' else 'clear')
            print(gone_rogue_logo)
            print("Welcome to Gone Rogue")
            break
        else:
            menu()


menu()

hero = entity.hero_init()

print("\033[A                             \033[A")
print("\033[A                             \033[A")

ent_dict = {'runt': ['runt', 5, 3], 'bruiser': ['bruiser', 10, 5],
            'boss': ['boss', 20, 7], 'lunch': ['lunch', 0, 5],
            'stimulant': ['stimulant', -2, 2], 'vigour': ['vigour', 0, 3]}

ent_names = list(ent_dict.keys())

l1 = [ent_dict['runt'], ent_dict[ent_names[randint(3, 5)]]]
l2 = [ent_dict['bruiser'], ent_dict[ent_names[randint(3, 5)]]]
l3 = [ent_dict['boss'], ent_dict[ent_names[randint(3, 5)]]]

enemy, loot, stairs = entity.ents_init(l1[0], l1[1])

map_limit = level.largest_index_position(hero.position, enemy.position,
                                         loot.position, stairs.position)
level_map = level.LevelMapGen(map_limit)
hero_map_att = [hero.h_p, hero.power, hero.icon, hero.position]
level_map.print_map(level_map.map, hero_map_att, enemy.position,
                    loot.position, stairs.position, gone_rogue_logo)
check_pos = 'walk'

move = input('\nWhere would you like to go...?\n')
check_pos, hero_index = level_map.move_hero(hero_map_att, move, level_map.map,
                                            map_limit)

hero_map_att[3] = hero_index
level_map.print_map(level_map.map, hero_map_att, enemy.position,
                    loot.position, stairs.position, gone_rogue_logo)


def battle():
    enemy.h_p -= hero.power
    print('\n')
    print(f'{hero.name} hits {enemy.name}. {enemy.name} hp: {enemy.h_p}')
    input()
    if enemy.h_p <= 0:
        print(f'You defeated {enemy.name}!')
    else:
        hero.h_p -= enemy.power
        hero_map_att[0] -= enemy.power
        print(f'{enemy.name} hits {hero.name}. {hero.name} hp: {hero.h_p}')
        input()
        print("\033[A                             \033[A")
        if hero.h_p < 0:
            print('Shit...')
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("""
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
      ░       ░  ░    ██▓███   ▄▄▄ ░     ██▓ ░   ▐██▌ ░     ░  ░   ░
                     ▓██░  ██▒▒████▄    ▓██▒     ▐██▌░
                     ▓██░ ██▓▒▒██  ▀█▄  ▒██░     ▐██▌
                     ▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██░     ▓██▒
                     ▒██▒ ░  ░ ▓█   ▓██▒░██████▒ ▒▄▄
                     ▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░▓  ░ ░▀▀▒
                     ░▒ ░       ▒   ▒▒ ░░ ░ ▒  ░ ░  ░
                     ░░         ░   ▒     ░ ░       ░
                                    ░  ░    ░  ░ ░""")
            input()
            print('CLICK RUN to play again.')
            sys.exit()
        elif enemy.h_p < 0:
            print(f'You defeated {enemy.name}!')
        else:
            battle()


def play_level(check_pos):
    while True:
        if check_pos == 'walk':
            move = input('\nWhere would you like to go...?\n')
            check_pos, hero_index = level_map.move_hero(hero_map_att, move,
                                                        level_map.map,
                                                        map_limit)
            hero_map_att[3] = hero_index
            level_map.print_map(level_map.map, hero_map_att, enemy.position,
                                loot.position, stairs.position,
                                gone_rogue_logo)
            continue
        if check_pos == 'loot':
            level_map.map[hero_index[0]][hero_index[1]] = hero.icon
            loot.position = stairs.position
            print(f'\nYou picked up {loot.name}!')
            if loot.name == 'lunch':
                level_map.map[hero_index[0]][hero_index[1]] = hero.icon
                hero.h_p += loot.power
                hero_map_att[0] += loot.power
                print("It's delicious...")
                print(f'You gained {loot.power} hp.')
            elif loot.name == 'stimulant':
                level_map.map[hero_index[0]][hero_index[1]] = hero.icon
                hero.power *= loot.power
                hero_map_att[1] *= loot.power
                hero.h_p += loot.h_p
                hero_map_att[0] += loot.h_p
                print('You feel way juiced, man! So juiced it hurts.')
                print('Your bloodied fists twitch, itching to get to work.')
            else:
                level_map.map[hero_index[0]][hero_index[1]] = hero.icon
                hero.power += loot.power
                hero_map_att[1] += loot.power
                print("Is that ginger and chilli?")
                print('WOW that packs a punch!')
            check_pos = 'walk'
            continue
        if check_pos == 'fight':
            battle()
            enemy.position = stairs.position
            check_pos = 'walk'
        elif check_pos == 'stairs':
            level_map.map[hero_index[0]][hero_index[1]] = hero.icon
            print('\nGoing down?')
            break
        elif check_pos == 'oob':
            os.system('cls' if os.name == 'nt' else 'clear')
            level_map.print_map(level_map.map, hero_map_att, enemy.position,
                                loot.position, stairs.position,
                                gone_rogue_logo)
            print("You walked into a wall.\n")
            move = input('Where would you like to go...?\n')
            check_pos, hero_index = level_map.move_hero(hero_map_att, move,
                                                        level_map.map,
                                                        map_limit)
            hero_map_att[3] = hero_index
            level_map.print_map(level_map.map, hero_map_att, enemy.position,
                                loot.position, stairs.position,
                                gone_rogue_logo)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            level_map.print_map(level_map.map, hero_map_att, enemy.position,
                                loot.position, stairs.position,
                                gone_rogue_logo)
            print('\nUse\nw - up\na - left\ns - down\nd -right\nto move...\n')
            move = input('Where would you like to go...?\n')
            check_pos, hero_index = level_map.move_hero(hero_map_att, move,
                                                        level_map.map,
                                                        map_limit)
            hero_map_att[3] = hero_index
            level_map.print_map(level_map.map, hero_map_att, enemy.position,
                                loot.position, stairs.position,
                                gone_rogue_logo)


play_level(check_pos)
input('PRESS ENTER to go deeper...')


# #################Level 2################# #

hero.position = [(randint(0, 6)), (randint(0, 6))]
hero_map_att[3] = hero.position
enemy, loot, stairs = entity.ents_init(l2[0], l2[1])

map_limit = level.largest_index_position(hero.position, enemy.position,
                                         loot.position, stairs.position)
level_map = level.LevelMapGen(map_limit)
hero_map_att = [hero.h_p, hero.power, hero.icon, hero.position]
level_map.print_map(level_map.map, hero_map_att, enemy.position,
                    loot.position, stairs.position, gone_rogue_logo)
check_pos = 'walk'

move = input('\nWhere would you like to go...?\n')
check_pos, hero_index = level_map.move_hero(hero_map_att, move, level_map.map,
                                            map_limit)
# print(check_pos, hero_index)

hero_map_att[3] = hero_index
level_map.print_map(level_map.map, hero_map_att, enemy.position, loot.position,
                    stairs.position, gone_rogue_logo)

play_level(check_pos)
input('PRESS ENTER to go deeper...')


# #################Level 3################# #

hero.position = [(randint(0, 6)), (randint(0, 6))]
hero_map_att[3] = hero.position
enemy, loot, stairs = entity.ents_init(l3[0], l3[1])

map_limit = level.largest_index_position(hero.position, enemy.position,
                                         loot.position, stairs.position)
level_map = level.LevelMapGen(map_limit)
hero_map_att = [hero.h_p, hero.power, hero.icon, hero.position]
level_map.print_map(level_map.map, hero_map_att, enemy.position, loot.position,
                    stairs.position, gone_rogue_logo)
check_pos = 'walk'

move = input('\nWhere would you like to go...?\n')
check_pos, hero_index = level_map.move_hero(hero_map_att, move, level_map.map,
                                            map_limit)

hero_map_att[3] = hero_index
level_map.print_map(level_map.map, hero_map_att, enemy.position, loot.position,
                    stairs.position, gone_rogue_logo)

play_level(check_pos)

os.system('cls' if os.name == 'nt' else 'clear')

print(f"""
Got what was coming to 'em.
Nobody steals {hero.name}'s property...""")
input()
input('\nSEARCH THE ROOM...')
print('\n*fumbling*...')
input()
print('I knew it...')
input()
os.system('cls' if os.name == 'nt' else 'clear')

print("""
              (((((((((((((
          /((((((       ((((((.
          /((((((       ((((((.
          /((((((       ((((((.
          /((((((       ((((((.
          /((((((       ((((((.
           ...(((///////(((...
              (((((((((((((
                 (((((((
          /(((((((((((((((((((.
           ......(((((((......
                 (((((((
                 (((((((""")
input()
print('...this asshole stole THE AMULET.')
input()
input('TAKE THE AMULET...')
print("\033[A                             \033[A")
print("This'll make a sweet offering in exchange for immortality...")
input()


os.system('cls' if os.name == 'nt' else 'clear')
print("CONGRATULATIONS")
print('You have...')

input()

print("""
  ▄████  ▒█████   ███▄    █ ▓█████
 ██▒ ▀█▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀
▒██░▄▄▄░▒██░  ██▒▓██  ▀█ ██▒▒███
░▓█  ██▓▒██   ██░▓██▒  ▐▌██▒▒▓█
░▒▓███▀▒░ ████▓▒░▒██░   ▓██░░▒████▒
 ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░
  ░   ░   ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░
░ ░   ░ ░ ░ ░ ▒     ░   ░ ░    ░
      ░     ░ ░           ░    ░  ░""")
input()
print("""
 ██▀███   ▒█████    ▄████  █    ██ ▓█████
▓██ ▒ ██▒▒██▒  ██▒ ██▒ ▀█▒ ██  ▓██▒▓█   ▀
▓██ ░▄█ ▒▒██░  ██▒▒██░▄▄▄░▓██  ▒██░▒███
▒██▀▀█▄  ▒██   ██░░▓█  ██▓▓▓█  ░██░▒▓█  ▄
░██▓ ▒██▒░ ████▓▒░░▒▓███▀▒▒▒█████▓ ░▒████▒
░ ▒▓ ░▒▓░░ ▒░▒░▒░  ░▒   ▒ ░▒▓▒ ▒ ▒ ░░ ▒░ ░
  ░▒ ░ ▒░  ░ ▒ ▒░   ░   ░ ░░▒░ ░ ░  ░ ░  ░
  ░░   ░ ░ ░ ░ ▒  ░ ░   ░  ░░░ ░ ░    ░
  ░         ░ ░        ░    ░        ░  ░""")
input()
print('CLICK RUN to play again.')
