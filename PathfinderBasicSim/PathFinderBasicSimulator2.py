class Character(object):
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

class Monster(Character):
    def __init__ (self, name, initiative, speed, challenge_rating, xp, hp_max, defense_ac,
                 defense_touch, defense_flatfooted, offense_melee, offense_melee_bonus, offense_melee_dice,
                 offense_melee_minimum, offense_melee_maximum, offense_melee_critchance,
                 stats_str, stats_dex, stats_con, stats_int, stats_wis, stats_cha):
        self.name = name
        self.initiative = initiative
        self.speed = speed
        self.challenge_rating = challenge_rating
        self.xp = xp
        self.hp_current = hp_max
        self.hp_max = hp_max
        self.ac_base = defense_ac
        self.ac_shield_bonus = 0
        self.ac_dex_mod = 0
        self.weapon_dmg_minimum = offense_melee_minimum
        self.weapon_dmg_maximum = offense_melee_maximum