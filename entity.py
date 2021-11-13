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
            h_name = input('What is your name hero?\n')
            if h_name[0].isalpha():
                hero = Ent(h_name, 15, 3, hero_position)
                return hero
                break
            else:
                print("That's an unusual name, would you mind anglicizing it...")
        except IndexError as e:
            print('But you must have a name?')

def ents_init(enemy_ent, loot_ent):
    enemy1_position = [(randint(0, 10)), (randint(0, 10))]

    a = hero_position
    b = enemy1_position

    while a == b:
        enemy1_position = [(randint(0, 10)), (randint(0, 10))]

    enemy_ent = Ent('#' + enemy_ent[0], enemy_ent[1], enemy_ent[2], enemy1_position)

    loot1_position = [(randint(0, 10)), (randint(0, 10))]
    c = loot1_position

    while c == a or c == b:
        loot1_position = [(randint(0, 10)), (randint(0, 10))]

    loot_ent = Ent('?' + loot_ent[0], loot_ent[1], loot_ent[2], loot1_position)

    stairs1_position = [(randint(0, 10)), (randint(0, 10))]
    d = stairs1_position

    while d == a or d == b or d == c:
        stairs1_position = [(randint(0, 10)), (randint(0, 10))]

    stairs = Ent('/stairs', 0, 0, stairs1_position)

    return vars(enemy_ent), vars(loot_ent), vars(stairs)
