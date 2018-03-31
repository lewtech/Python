class Archetype(object):
    def __init__(self, name = "archetype", character_class = "archetype"):
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

        def attack(opponent:Archetype):
            print(name + " attacks!")


class Fighter(Archetype):
    def __init__(self, name, character_class):
        super(Archetype, self).__init__()
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



        def attack(opponent):
            pass

archetype = Archetype()
fighter = Fighter("testclass","murderer")
print(fighter.name)
print(archetype.name)
archetype.attack(fighter)