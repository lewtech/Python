import TDD_Char_Builder
import TDD_Char_View
import TDD_Char_Controller


cb = TDD_Char_Builder
tv = TDD_Char_View
cc = TDD_Char_Controller


print(cb.roll4d6())
print ("from tdd tool" +  str(tv.roll_from_tddview()))

# create hero and enemy
testCharacter = cc.create_character("blood","fighter")
print(testCharacter.name + " " + testCharacter.character_class)
print(testCharacter.weapon)

testMonster = cc.create_monster("goblin","goblingrunt")
print(testMonster.name + " " +testMonster.character_class)
cc.combatRound(testCharacter, testMonster, 5, "weapon", 10, 15, 1)
cc.combatRound(testMonster, testCharacter, 5, "weapon", 10, 15, 5)
cc.combatRound(testCharacter, testMonster, 5,"weapon", 10, 15, 10)
cc.combatRound(testCharacter, testMonster, 5,"weapon", 10, 15, 10)
#combat
#combat array




