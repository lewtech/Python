import random


class PlayerCharacter(object):
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class


def main():
    generate_abilities()
    gather_info()
    save_to_data()


def gather_info():
    print("\n")
    name = input("What is thy character's name? ")
    gameclass = input("What path shall thou travel? ")


def roll(sides):
    die_roll = random.randint(1, sides)
    return die_roll


def roll4d6():
    cache = []
    diesum = 0
    for i in range (0,4):
        roll_1d6 = roll(6)
        cache.append(roll_1d6)
        diesum = diesum + roll_1d6
    return diesum-min(cache)


def roll_numdice_die(numdice,die):
    diesum = 0
    for i in range (0,numdice):
        roll(die)
        diesum = diesum + roll(die)
    return sum


def generate_abilities():
    #1.0 this is a bad function. too big
    # generating scores, calculating what classes are available, and printing
    # it might be better to make the abilities into a class?
    bad_score = 7
    min_score = 13
    elite_score = 16
    ability_list = []
    print("   str dex con int wis cha")
    for i in range (0,8):
        classes = []
        class_options = []

        print(str(i+1) + ":", end = " ")
        for j in range(0, 6):
            score = roll4d6()
            if score >= 10:
                print (score, end = "  ")
            if score < 10 :
                print ("0" + str(score), end = "  ")

            if j == 0:
                if score >= min_score:
                    class_options = "fighter/barbarian"
                if score >= elite_score:
                    class_options = class_options.upper()
                if score <= bad_score:
                    class_options = "weakling"
                classes.append(str(class_options)) if class_options != [] else False
                class_options = []

            if j == 1:
                if score >= min_score:
                    class_options = "rogue/ranger"
                if score >= elite_score:
                    class_options = class_options.upper()
                if score <= bad_score:
                    class_options = "clumsy"
                classes.append(str(class_options)) if class_options != [] else False
                class_options = []
            if j == 3:
                if score >= min_score:
                    class_options = "wizard"
                if score >= elite_score:
                    class_options = class_options.upper()
                if score <= bad_score:
                    class_options = "peabrain"
                classes.append(str(class_options)) if class_options != [] else False
                class_options = []
            if j == 4:
                if score >= min_score:
                    class_options = "cleric/druid"
                if score >= elite_score:
                    class_options = class_options.upper()
                if score <= bad_score:
                    class_options = "buffoon"
                classes.append(str(class_options)) if class_options != [] else False
                class_options = []
            if j == 5:
                if score >= min_score:
                    class_options = "sorcerer/bard"
                if score >= elite_score:
                    class_options = class_options.upper()
                if score <= bad_score:
                    class_options = "outcast"
                classes.append(str(class_options)) if class_options != [] else False
                print (str(classes) + "\n")
                class_options = []


def save_to_data():
    pass


main()






#lets use this as an exercise in parsing lists of lists
#rolls will be [[9,10,22,21,2,3]]