import random



class Character(object):
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.meleer = True
        self.hp = 10
        self.hp_max = 50
        self.hp_curr = 50
        self.weapon = "blade"
        self.attack = self.weapon
        self.weapon_die = 8
        self.weapon_numberOfDice = 1
        self.ranged_minimum = 10
        self.ranged_maximum = 100
        self.ranged_weapon_die = 6
        self.position = 5
        self.surprised = False
        self.hero = True
        # archetypes of hero: shield, sword, arrow, shadow, arcane, divine





class Monster(object):
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.meleer = True
        self.hp = 10
        self.hp_max = 10
        self.hp_curr = 10
        self.weapon = "claw"
        self.attack = self.weapon
        self.weapon_die = 8
        self.weapon_numberOfDice = 1
        self.position = 50
        self.surprised = False
        self.hero = False

class battleground:
    def __init__(self, name, area_number, size, monster, trap, treasure, storypoint):
        self.name = name
        self.area_number = area_number
        self.size = size
        self.monster = monster
        self.trap = trap
        self.treasure = treasure
        self.storypoint = storypoint




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
    if combatant1.meleer == True:
        if (combatant2.position - combatant1.position) > 5:
            move_check_distance(combatant1, combatant2, move)
    # if (combatant2.position - combatant1.position)  <=  5:

        print(combatant1.name + " swings at " + combatant2.name, "with their " + combatant1.attack + " for " + str(damage) + " points of damage" )
        combatant2.hp_curr = combatant2.hp_curr - damage
        print(combatant2.name + " current hp : " + str(combatant2.hp_curr) + "/" +str(combatant2.hp_max) + " Position: " + str(combatant2.position))
        print("--------")


def move_check_distance(combatant1: object, combatant2, move: int):
    if (combatant2.position - combatant1.position) > 1:
        combatant1.position = combatant1.position + move

    else :
        combatant1.position = combatant1.position - move
        if combatant1.position < 0:
            combatant1.position = 0


def combatant_dead(combatant):
    print(combatant.name + " is dead")

# testCharacter = create_character("one", "mage")
# testMonster = create_character("two", "fighter")
# combatRound(testCharacter, testMonster, 0,"weapon", 10, 15, 10)