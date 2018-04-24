import archetypes

a = archetypes

# initialize characters
# roll initiative
# create arrays
# initiative array, hero array, enemy array

def main():
    archetype = a.Archetype()
    fighter = a.Melee("Tribolio","murderer")
    goblin = a.Goblin("goblin","goblin")
    goblin.position = 100
    continue_combat = True
    for i in range (0, 8):
        a.combat(fighter, goblin)
        a.combat(goblin, fighter)

main()