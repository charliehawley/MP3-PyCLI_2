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
            print('You must have a name?')