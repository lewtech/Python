import TDD_Char_Builder
import TDD_Char_View
import TDD_Char_Controller


cb = TDD_Char_Builder
tv = TDD_Char_View
cc = TDD_Char_Controller

combat_status = False


print(cb.roll4d6())
print ("from tdd tool" +  str(tv.roll_from_tddview()))
'''
This is a rpg simulator, the eventual goal is to be able to  load up different monsters and heroes
they will duke it out and something comes out as the winner. I think it might be possible to create
a space version as well. Later I can also load randomly generating components.
'''

# create hero and enemy
# testCharacter = cc.create_character("blood","fighter")
# print(testCharacter.name + " " + testCharacter.character_class)
# print(testCharacter.weapon)
#
# testMonster = cc.create_monster("goblin","goblingrunt")
# print(testMonster.name + " " +testMonster.character_class)
# cc.combatRound(testCharacter, testMonster, 5, "weapon", 10, 15, 1)
# cc.combatRound(testMonster, testCharacter, 5, "weapon", 10, 15, 5)
# cc.combatRound(testCharacter, testMonster, 5,"weapon", 10, 15, 10)
# cc.combatRound(testCharacter, testMonster, 5,"weapon", 10, 15, 10)
#combat
#combat array

test_initiative_hero = cc.create_character("fighter", "fighter")
test_initiative_hero2 = cc.create_character("mage", "fighter")
test_initiative_creature1 = cc.create_monster("goblin1", "goblinord")
test_initiative_creature2 = cc.create_monster("goblin2", "goblinord")
test_initiative_creature3 = cc.create_monster("goblin3", "goblinord")
test_initiative_creature4 = cc.create_monster("goblin4", "goblinord")
test_initiative_creature5 = cc.create_monster("goblin5", "goblinord")
turn_array = []
# 1) check surprise
def char_check_surprise(creature):
    if creature.surprised == False:
        pass

# 2) everyone roll initiative (1d20+initiative bonus)
def roll_inititiative():
    pass

# 3) add everyone to initiave array or turn sequence
hero_array = []
enemy_array = []
initiative_lineup = []
initiative_lineup.append(test_initiative_hero)
initiative_lineup.append(test_initiative_hero2)
print("initiative hero")
initiative_lineup.append(test_initiative_creature1)
initiative_lineup.append(test_initiative_creature2)
initiative_lineup.append(test_initiative_creature3)
initiative_lineup.append(test_initiative_creature4)
initiative_lineup.append(test_initiative_creature5)
print("initiative enemy")
def hero_and_enemy_array(initiative_lineup):
    print(initiative_lineup)
    for i in initiative_lineup:
        if i.hero == True:
            hero_array.append(i)
            print("add hero to hero array")

        else:
            enemy_array.append(i)
            print("add enemy to enemy array")


# 4) in initiative order, everyone takes a turn, surprised cannot take an action the first round...repeat step 4
# pick an enemy
def pick_enemy():
    pass

def initiative_attack():
    if enemy_array == [] or hero_array == []:
        print("combat done" + str(initiative_lineup))
        return

    for i in initiative_lineup:
        attack_with = i
        if attack_with.hero == True:
            attack_enemy = enemy_array[0]
        if attack_with.hero == False:
            attack_enemy = hero_array[0]
        if (attack_enemy.position - attack_with.position) > 5:
            cc.move_check_distance(attack_with, attack_enemy, 5)

        # if (attack_enemy.position - attack_with.position) <= 5:
            if (attack_enemy.position - attack_with.position) > 5:
                cc.move_check_distance(attack_with, attack_enemy, 5)
            cc.combatRound(attack_with, attack_enemy, 5, "weapon", 10, 15, 5)
        if attack_enemy.hp_curr < 1:
            # enemy_array.remove(attack_enemy)
            # initiative_lineup.remove(attack_enemy)
            remove_attack_enemy(attack_enemy)
            print ("dead")



def remove_attack_enemy(attack_enemy):
    print("REMOVE " + str(attack_enemy))
    if initiative_lineup != [] or enemy_array != []:
        initiative_lineup.remove(attack_enemy)
        if attack_enemy.hero == False:
            enemy_array.remove(attack_enemy)
        if attack_enemy.hero == True:
            hero_array.remove(attack_enemy)

def sort_arrays():
    pass

def check_range():
    pass

hero_and_enemy_array(initiative_lineup)
combat_status = True
print("combat status " + str(combat_status))
while len(initiative_lineup) > 1:
    sort_arrays()
    check_range()
    initiative_attack()

# next begin adding range to attack
# check range
# if in melee range attack
# if melee move forward
# if ranged move backward
# if stealth try stealth
#test










