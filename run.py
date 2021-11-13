import entity
from random import randint

hero = entity.hero_init()

ent_dict = {'runt': ['runt', 3, 2], 'bruiser': ['bruiser', 4, 3], 'boss': ['boss', 10, 4], 'lunch': ['lunch',0, 5], 
'stimulant': ['stimulant', 0, 2], 'vigour': ['vigour', 0, 5]}

ent_names = list(ent_dict.keys())

l1 = [ent_dict['runt'], ent_dict[ent_names[randint(3, 5)]]]
l2 = [ent_dict['bruiser'], ent_dict[ent_names[randint(3, 5)]]]
l3 = [ent_dict['boss'], ent_dict[ent_names[randint(3, 5)]]]

print(l1)
print(l2)
print(l3)

ents = entity.ents_init(l1[0], l1[1])
