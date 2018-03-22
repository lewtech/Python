import random



class Character(object):
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.hp = 10
        self.hp_max = 10
        self.hp_curr = 10
        self.weapon = "blade"
        self.attack = self.weapon
        self.weapon_die = 8
        self.weapon_numberOfDice = 1
        self.position = 5

class Monster(object):
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.hp = 10
        self.hp_max = 10
        self.hp_curr = 10
        self.weapon = "claw"
        self.attack = self.weapon
        self.weapon_die = 8
        self.weapon_numberOfDice = 1
        self.position = 15




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
    player = Character(name, character_class)
    return player

def create_monster(name, character_class):
    monster = Monster(name, character_class)
    return monster





def combatRound(combatant1, combatant2, move, weapon, ac, tohitroll, damage):
    #movement

    if combatant2.hp_curr < 1:
        combatant_dead(combatant2)
        return False
    move_check_distance(combatant1, combatant2, move)
    print(combatant1.name + " swings at " + combatant2.name, "with their " + combatant1.attack + " for " + str(damage) + " points of damage" )
    combatant2.hp_curr = combatant2.hp_curr - damage
    print(combatant2.name + " current hp : " + str(combatant2.hp_curr) + "/" +str(combatant2.hp_max) + " Position: " + str(combatant2.position))
    print("--------")


def move_check_distance(combatant1: object, combatant2, move: int):
    if (combatant2.position - combatant1.position) > 1:
        combatant1.position = combatant1.position + move
    else :
        combatant1.position = combatant1.position - move
        pass

def combatant_dead(combatant):
    print(combatant.name + " is dead")

# testCharacter = create_character("one", "mage")
# testMonster = create_character("two", "fighter")
# combatRound(testCharacter, testMonster, 0,"weapon", 10, 15, 10)