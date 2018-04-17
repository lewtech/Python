def move(self, opponent, advance):
    if advance == True:
        movement = 5
    if advance == False:
        movement = -5
    if self.position < opponent.position:
        self.position = self.position + movement
    if self.position > opponent.position:
        self.position = self.position - movement
    print("{} advances!".format(self.name))

def combat_round(self, opponent):
    opponent.hp_curr = opponent.hp_curr - self.weapon_die
    print(
        "{} {} his {} at {} doing {} points of damage!".format(self.name, self.attack_type, self.weapon, opponent.name,
                                                               self.weapon_die))
    print("{} loses {} health points!".format(opponent.name, self.weapon_die))


class Archetype:
    def __init__(self, name = "archetype", character_class = "archetype"):
        self.name = name
        self.character_class = character_class
        self.meleer = True
        self.hp = 10
        self.hp_max = 50
        self.hp_curr = 50
        self.weapon = "blade"
        self.attack_type = "swings"
        self.weapon_die = 8
        self.weapon_numberOfDice = 1
        self.ranged_minimum = 10
        self.ranged_maximum = 100
        self.ranged_weapon_die = 6
        self.position = 5
        self.surprised = False
        self.hero = True
        self.melee_distance = 5
        # types of hero: shield, sword, arrow, shadow, arcane, divine

# let's make an omnibus function that uses ranged modifiers and things to calculate which step to do.
    def attack(self, opponent):
        distance = abs(self.position - opponent.position)
        #print ("distance between {} and {} is {}".format(self.name, opponent.name, distance))
        if distance <= self.melee_distance:
            combat_round(self, opponent)
        else:
            move(self, opponent, True)




class Melee(Archetype):
    pass


class Ranged(Archetype):
    def __init__(self, name, character_class):
        Archetype.__init__(self, name , character_class )
        self.weapon = "rock"
        self.attack_type = "throws"
    def attack(self, opponent):
        distance = abs(self.position - opponent.position)
        #print ("distance between {} and {} is {}".format(self.name, opponent.name, distance))
        if distance <= self.ranged_maximum:
            combat_round(self, opponent)
        else:
            move(self, opponent, False)

class Goblin(Ranged):
    # Ranged.__init__(self)
    # self.weapon = "blade"
    # self.attack_type = "swings"
    pass



class Rogue(Archetype):
    pass


class Mage(Archetype):
    pass


class Divine(Archetype):
    pass






archetype = Archetype()
fighter = Melee("Tribolio","murderer")
goblin = Ranged("goblin","goblin")
goblin.position = 100

while goblin.hp_curr > 0 or fighter.hp_curr > 0:
    fighter.attack(goblin)
    goblin.attack(fighter)