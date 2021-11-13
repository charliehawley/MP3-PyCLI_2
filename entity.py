from random import randint

class Ent:
    def __init__(self, name, hp, power, position):
        self.name = name
        self.hp = hp
        self.power = power
        self.icon = name[0]
        self.position = position