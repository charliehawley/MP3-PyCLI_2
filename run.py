import os
import sys
from random import randint
import entity
import level


CHECK_POS = 'walk'
GONE_ROGUE_LOGO = """
  ▄████  ▒█████   ███▄    █ ▓█████     ██▀███   ▒█████    ▄████  █    ██ ▓█████
 ██▒ ▀█▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀    ▓██ ▒ ██▒▒██▒  ██▒ ██▒ ▀█▒ ██  ▓██▒▓█   ▀
▒██░▄▄▄░▒██░  ██▒▓██  ▀█ ██▒▒███      ▓██ ░▄█ ▒▒██░  ██▒▒██░▄▄▄░▓██  ▒██░▒███
░▓█  ██▓▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄    ▒██▀▀█▄  ▒██   ██░░▓█  ██▓▓▓█  ░██░▒▓█  ▄
░▒▓███▀▒░ ████▓▒░▒██░   ▓██░░▒████▒   ░██▓ ▒██▒░ ████▓▒░░▒▓███▀▒▒▒█████▓ ░▒████
░▒   ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░  ░▒   ▒ ░▒▓▒ ▒ ▒ ░░ ▒░
░   ░   ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░     ░▒ ░ ▒░  ░ ▒ ▒░   ░   ░ ░░▒░ ░ ░  ░ ░
░ ░   ░ ░ ░ ░ ▒     ░   ░ ░    ░        ░░   ░ ░ ░ ░ ▒  ░ ░   ░  ░░░ ░ ░    ░
    ░     ░ ░           ░    ░  ░      ░         ░ ░        ░    ░        ░"""

ent_dict = {'runt': ['runt', 5, 3], 'bruiser': ['bruiser', 10, 5],
            'boss': ['boss', 20, 7], 'lunch': ['lunch', 0, 5],
            'stimulant': ['stimulant', -2, 2], 'vigour': ['vigour', 0, 3]}

ent_names = list(ent_dict.keys())

l1 = [ent_dict['runt'], ent_dict[ent_names[randint(3, 5)]]]
l2 = [ent_dict['bruiser'], ent_dict[ent_names[randint(3, 5)]]]
l3 = [ent_dict['boss'], ent_dict[ent_names[randint(3, 5)]]]

enemy, loot, stairs = entity.ents_init(l1[0], l1[1])


def menu():
    """
    Handles UI for the title screen of Gone Rogue

        ARGS: strings - 'i', 'h', 's'

        RETURNS: - introduction to the game and its historical context
            or   - instructions describing how to interact with the game
            or   - starts the game loop"""

    # clears game screen
    os.system('cls' if os.name == 'nt' else 'clear')
    # prints title
    print(GONE_ROGUE_LOGO)
    print("Welcome to Gone Rogue")
    # creates menu loop
    while True:
        menu_choice = input('\ni = intro, h = how to play, s = start\n')

        # on user input 'i' prints introduction
        if menu_choice == 'i':
            # print statements with values of ("\033[A \033[A")
            # remove the line above
            print("\033[A                                            \033[A")
            print("\033[A                                            \033[A")
            print("\033[A                                            \033[A\n")
            print("""
    The year is 1980. Miami is burning, Post-Its just hit the shelves,
    the MGM is on fire and somebody just shot John Lennon.
    PRESS ENTER""")
            # empty input to allow user to cue the next line when they're ready
            input()
            print("\033[A                             \033[A")
            print("\033[A                             \033[A")
            print("""
    The world is chaotic and unpredictable.
    Will there be peace? Will there be justice? Will there be revolution?
            """)
            input()
            print("\033[A                             \033[A")
            print("\033[A                             \033[A")
            print("""
    Enter procedural generation,
    a way of producing 'randomised' worlds from stable rules.""")
            input()
            print("\033[A                             \033[A")
            print("""
    This is the world of Rogue, the original Roguelike game
    that bore an entire genre dedicated to those seeking to witness
    the illusion of control shattering before them.""")
            input()
            print("\033[A                             \033[A")
            print("""
    It gave them something they had never seen before.
    The game had agency, a life of its own.""")
            input()
            print("\033[A                             \033[A")
            print("""
    Now, 40 years later, entropy has flaunted its inescapable will
    and laid waste to the already waning optimism of the mid 20th Century.""")
            input()
            print("\033[A                             \033[A")
            print("""\n    The only cure?
    Surrendering yourself to endless possibility.""")
            input()
            print("\033[A                             \033[A")
            print("""\n    Some can follow their instincts
    and get their hands dirty.""")
            input()
            print("\033[A                             \033[A")
            print("\n    Others fall behind trying to reason with the chaos.")
            input()
            print("\033[A                             \033[A")
            print("\n    How will you fare in the bloody world of GONE ROGUE?")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
            print(GONE_ROGUE_LOGO)
            print("Welcome to Gone Rogue")

        # prints instructions on how to play the game
        elif menu_choice == 'h':
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
            input('     PRESS ENTER...\n')
            print(GONE_ROGUE_LOGO)
            print("Welcome to Gone Rogue")

        # breaks out of menu loop
        elif menu_choice == 's':
            print("\033[A \033[A")
            print('It begins...')
            input()

            os.system('cls' if os.name == 'nt' else 'clear')
            print(GONE_ROGUE_LOGO)
            print("Welcome to Gone Rogue")
            break
        else:
            print("Try 'i', 'h' or 's'")
            input()

            print("\033[A                                      \033[A")
            print("\033[A                                      \033[A")
            print("\033[A                                      \033[A")
            print("\033[A                                      \033[A")
            print("\033[A                                      \033[A")


def battle():
    """
    Handles encounter between hero and enemy

        ARGS: object attributes - (hero.h_p, hero.power,
                                   enemy.h_p, enemy.power)

        RETURNS: - update's hero objects hp
                 - prints outcome of battle
    """
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
            input()
        else:
            battle()


def play_level(state):
    """
    Handles the game loop

        ARGS: string - describes the state of the hero's current position

        RETURNS: - prints dialogue for each encounter
                 - updates hero position
                 - updates hero power
                 - breaks game loop when stairs encountered
                 - validates user input"""
    while True:
        if state == 'walk':
            move = input('\nWhere would you like to go...?\n')
            state, hero_index = level.move_hero(hero_map_att, move,
                                                level_map.map, map_limit)
            hero_map_att[3] = hero_index
            level.print_map(level_map.map, hero_map_att, enemy.position,
                            loot.position, stairs.position, GONE_ROGUE_LOGO)
            continue
        if state == 'loot':
            level_map.map[hero_index[0]][hero_index[1]] = hero.icon
            loot.position = stairs.position
            print(f'\nYou picked up {loot.name}!')
            if loot.name == 'lunch':
                level_map.map[hero_index[0]][hero_index[1]] = hero.icon
                hero.h_p += loot.power
                hero_map_att[0] += loot.power
                print("It's delicious...")
                print(f'You gained {loot.power} hp.')
                input()
                print("\033[A                                      \033[A")
                print("\033[A                                      \033[A")
                print("\033[A                                      \033[A")
                print("\033[A                                      \033[A")
                print("\033[A                                      \033[A")
            elif loot.name == 'stimulant':
                level_map.map[hero_index[0]][hero_index[1]] = hero.icon
                hero.power *= loot.power
                hero_map_att[1] *= loot.power
                hero.h_p += loot.h_p
                hero_map_att[0] += loot.h_p
                print('''You feel way juiced, man!
So juiced it hurts.''')
                print('''Your bloodied fists twitch,
itching to get to work.''')
                input()
                print("\033[A                                          \033[A")
                print("\033[A                                          \033[A")
                print("\033[A                                          \033[A")
                print("\033[A                                          \033[A")
                print("\033[A                                          \033[A")
                print("\033[A                                          \033[A")
                print("\033[A                                          \033[A")
            else:
                level_map.map[hero_index[0]][hero_index[1]] = hero.icon
                hero.power += loot.power
                hero_map_att[1] += loot.power
                print("Is that ginger and chilli?")
                print('WOW that packs a punch!')
                input()
                print("\033[A                                      \033[A")
                print("\033[A                                      \033[A")
                print("\033[A                                      \033[A")
                print("\033[A                                      \033[A")
                print("\033[A                                      \033[A")
            state = 'walk'
            continue
        if state == 'fight':
            battle()
            enemy.position = stairs.position
            state = 'walk'
        elif state == 'stairs':
            level_map.map[hero_index[0]][hero_index[1]] = hero.icon
            print('\nGoing down?')
            break
        elif state == 'oob':
            os.system('cls' if os.name == 'nt' else 'clear')
            level.print_map(level_map.map, hero_map_att, enemy.position,
                            loot.position, stairs.position, GONE_ROGUE_LOGO)
            print("You walked into a wall.\n")
            move = input('Where would you like to go...?\n')
            state, hero_index = level.move_hero(hero_map_att, move,
                                                level_map.map, map_limit)
            hero_map_att[3] = hero_index
            level.print_map(level_map.map, hero_map_att, enemy.position,
                            loot.position, stairs.position, GONE_ROGUE_LOGO)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            level.print_map(level_map.map, hero_map_att, enemy.position,
                            loot.position, stairs.position, GONE_ROGUE_LOGO)
            print('\nUse\nw - up\na - left\ns - down\nd -right\nto move...\n')
            move = input('Where would you like to go...?\n')
            state, hero_index = level.move_hero(hero_map_att, move,
                                                level_map.map, map_limit)
            hero_map_att[3] = hero_index
            level.print_map(level_map.map, hero_map_att, enemy.position,
                            loot.position, stairs.position, GONE_ROGUE_LOGO)


def success():
    """
    Prints dialogue after level 3 game loop is broken
    and directs user to the run button should they want to replay"""
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"""
        Got what was coming to 'em.
        Nobody steals {hero.name}'s property...""")
    input()
    input('\nSEARCH THE ROOM...')

    print('\n*fumbling*...')
    input()

    print('    I knew it...')
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

    print('    ...this asshole stole THE AMULET.')
    input()
    input('TAKE THE AMULET...\n')

    print("\033[A                             \033[A")
    print("\033[A                             \033[A")
    print("    This'll make a sweet offering in exchange for immortality...")
    input()

    os.system('cls' if os.name == 'nt' else 'clear')
    print("    CONGRATULATIONS")
    print('    You have...')
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


menu()

hero = entity.hero_init()
hero_index = hero.position

print("\033[A                             \033[A")
print("\033[A                             \033[A")

# #################Level 1################# #
map_limit = level.largest_index_position(hero.position, enemy.position,
                                         loot.position, stairs.position)
level_map = level.LevelMapGen(map_limit)
hero_map_att = [hero.h_p, hero.power, hero.icon, hero.position]
level.print_map(level_map.map, hero_map_att, enemy.position,
                loot.position, stairs.position, GONE_ROGUE_LOGO)

play_level(CHECK_POS)

input('PRESS ENTER to go deeper...\n')


# #################Level 2################# #

hero.position = [(randint(0, 6)), (randint(0, 6))]
hero_map_att[3] = hero.position
enemy, loot, stairs = entity.ents_init(l2[0], l2[1])

map_limit = level.largest_index_position(hero.position, enemy.position,
                                         loot.position, stairs.position)
level_map = level.LevelMapGen(map_limit)
hero_map_att = [hero.h_p, hero.power, hero.icon, hero.position]
level.print_map(level_map.map, hero_map_att, enemy.position,
                loot.position, stairs.position, GONE_ROGUE_LOGO)

move = input('\nWhere would you like to go...?\n')
CHECK_POS, hero_index = level.move_hero(hero_map_att, move, level_map.map,
                                        map_limit)

hero_map_att[3] = hero_index
level.print_map(level_map.map, hero_map_att, enemy.position, loot.position,
                stairs.position, GONE_ROGUE_LOGO)

play_level(CHECK_POS)

input('PRESS ENTER to go deeper...\n')


# #################Level 3################# #

hero.position = [(randint(0, 6)), (randint(0, 6))]
hero_map_att[3] = hero.position
enemy, loot, stairs = entity.ents_init(l3[0], l3[1])

map_limit = level.largest_index_position(hero.position, enemy.position,
                                         loot.position, stairs.position)
level_map = level.LevelMapGen(map_limit)
hero_map_att = [hero.h_p, hero.power, hero.icon, hero.position]
level.print_map(level_map.map, hero_map_att, enemy.position, loot.position,
                stairs.position, GONE_ROGUE_LOGO)

move = input('\nWhere would you like to go...?\n')
CHECK_POS, hero_index = level.move_hero(hero_map_att, move, level_map.map,
                                        map_limit)

hero_map_att[3] = hero_index
level.print_map(level_map.map, hero_map_att, enemy.position, loot.position,
                stairs.position, GONE_ROGUE_LOGO)

play_level(CHECK_POS)

success()
