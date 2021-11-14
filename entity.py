from random import randint

class Ent:
    def __init__(self, name, hp, power, position):
        self.name = name
        self.hp = hp
        self.power = power
        self.icon = name[0]
        self.position = position

hero_position = [(randint(0, 10)), (randint(0, 10))]

def hero_init():
    while True:
        try: 
            h_name = input('\nWhat is your name hero?\n')
            if h_name[0].isalpha():
                hero = Ent(h_name, 15, 3, hero_position)
                return hero
                break
            else:
                print("That's an unusual name, would you mind anglicizing it...")
        except IndexError as e:
            print('But you must have a name?')

def ents_init(enemy_ent, loot_ent):
    enemy_position = [(randint(0, 10)), (randint(0, 10))]

    a = hero_position
    b = enemy_position

    while a == b:
        enemy_position = [(randint(0, 10)), (randint(0, 10))]

    enemy_ent = Ent(enemy_ent[0], enemy_ent[1], enemy_ent[2], enemy_position)

    loot_position = [(randint(0, 10)), (randint(0, 10))]
    c = loot_position

    while c == a or c == b:
        loot_position = [(randint(0, 10)), (randint(0, 10))]

    loot_ent = Ent(loot_ent[0], loot_ent[1], loot_ent[2], loot_position)

    stairs_position = [(randint(0, 10)), (randint(0, 10))]
    d = stairs_position

    while d == a or d == b or d == c:
        stairs_position = [(randint(0, 10)), (randint(0, 10))]

    stairs = Ent('stairs', 0, 0, stairs_position)

    return enemy_ent, loot_ent, stairs
