import random


class PlayerCharacter(object):
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        hp = 10
        hp_max = 10
        hp_curr = 10
        weapon = "blade"
        weapon_die = 8
        weapon_numberOfDice = 1




def roll4d6():
    cache = []
    diesum = 0
    for i in range(0, 4):
        roll_1d6 = roll(6)
        cache.append(roll_1d6)
        diesum = diesum + roll_1d6
    return diesum - min(cache)


def roll(sides):
    die_roll = random.randint(1, sides)
    return die_roll

def create_character(name, character_class):
    player = PlayerCharacter(name, character_class)

    return player


