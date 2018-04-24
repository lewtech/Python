class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

        self.character_class = "test"
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

    def attack(self, opponent):
        other_guy.health = opponent.health - self.damage
        print("{} attacks {}!".format(self.name, opponent.name))
        print("{} loses {} health points!".format(opponent.name, self.damage))

    def __str__(self):
        return "{}: {}".format(self.name, self.health)

class Boxer(Fighter):
    def __init__(self, name):
        Fighter.__init__(self,name)
        self.health = 500
    def heal(self):
        self.health += 10

qazi = Fighter("quazi")
you = Boxer("lew")

print(qazi)
print(you)

you.attack(qazi)

