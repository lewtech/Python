import random



class PlayerCharacter(object):
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.hp = 10
        self.hp_max = 10
        self.hp_curr = 10
        self.weapon = "blade"
        self.weapon_die = 8
        self.weapon_numberOfDice = 1


class Monster(PlayerCharacter):
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.hp = 10
        self.hp_max = 10
        self.hp_curr = 10
        self.weapon = "blade"
        self.weapon_die = 8
        self.weapon_numberOfDice = 1


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


def create_monster(name, character_class):
    monster = Monster(name, character_class)
    return monster


def combatRound(combatant1, combatant2, weapon, ac, tohitroll, damage):
    print(combatant1.name + " swings at " + combatant2.name, "with their " + combatant1.weapon + " for " + str(damage) + " points of damage" )
    combatant2.hp_curr = combatant2.hp_curr - damage
    print(combatant2.name + " current hp : " + str(combatant2.hp_curr) + "/" +str(combatant2.hp_max))
    return combatant2