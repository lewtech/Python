import random

combat = False


class Player(object):
    def __init__(self, name, heroclass, level, str, dex, con, int, wis, cha):
        self.name = name
        self.heroclass = "fighter"
        self.level = 1
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.feat_cleave = True
        self.feat_cleave_left = 1
        self.ac_base = 10
        self.ac_shield_bonus = 0
        self.ac_dex_mod = 0
        self.hp_max = 10
        self.hp_current = 10
        self.weapon_name = "sword"
        self.weapon_bonus_to_hit = 2
        self.weapon_bonus_to_damage = 2
        self.weapon_dmg_minimum = 1
        self.weapon_dmg_maximum = 8
        self.shield = True
        self.shield_bonus = 2

    def calc_attack (self):
        self.attack = self.weapon_bonus_to_hit
        return self.attack



class Monster(object):
    def __init__(self, name, initiative, speed, challenge_rating, xp, hp_max, defense_ac,
                 defense_touch, defense_flatfooted, offense_melee, offense_melee_bonus, offense_melee_dice,
                 offense_melee_minimum, offense_melee_maximum, offense_melee_critchance,
                 stats_str, stats_dex, stats_con, stats_int, stats_wis, stats_cha):
        self.name = name
        self.speed = speed
        self.challenge_rating = challenge_rating
        self.xp = xp
        self.hp_max = hp_max
        self.hp_current = hp_max

        self.initiative = initiative
        self.speed = speed

        self.defense_ac = defense_ac
        self.defense_touch = defense_touch
        self.defense_flatfooted = defense_flatfooted
        self.offense_melee = offense_melee
        self.offense_melee_bonus = offense_melee_bonus
        self.offense_melee_dice = offense_melee_dice
        self.offense_melee_minimum = offense_melee_minimum
        self.offense_melee_maximum = offense_melee_maximum
        self.offense_melee_critchance = offense_melee_critchance
        self.stats_str = stats_str
        self.stats_dex = stats_dex
        self.stats_con = stats_con
        self.stats_int = stats_int
        self.stats_wis = stats_wis
        self.stats_cha = stats_cha

player1 = Player("blood", "fighter", 4, 18, 12, 15, 8, 10, 13)
goblin1 = Monster("goblin", 6, 30, .33, 325, 6, 16, 13, 14, "short sword", 2, 1, 1, 4, 10, 0, 2, 1, 0, -1, -2)

print(player1)
print(goblin1)

def roll(sides):
    roll = random.randint(1,sides)
    return roll


print (roll(20))



#roll initiative
#check surprise
#everyone roll intiative
#everyone in initiative order
#4everyone takes a turn in initiative order
combat = True
while combat == True:
    if roll(20) > goblin1.defense_ac:
        damage = roll(10)
        goblin1.hp_current = goblin1.hp_current - damage
        print("hero swings at goblin for " + str(damage) + " points of damage")
        if goblin1.hp_current < 1:
            print('goblin is dead')
            combat = False
            break



    else:
        print ("hero misses")
    if roll(20) > (player1.ac_base + player1.ac_dex_mod + player1.ac_shield_bonus):
        damage = roll(goblin1.offense_melee_dice)
        player1.hp_current = player1.hp_current - damage
        print("goblin swings at hero for " + str(damage) + " points of damage")
        if player1.hp_current < 1:
            print('hero dies!')
            combat = False
            break


    else:
        print ("goblin misses")

#5return to step 4

#turn
#standard action
    #melee 1d20 + attack_bonus + str_mod + other_mod
    #ranged 1d20 + attack_bonus + str_mod + other_mod


