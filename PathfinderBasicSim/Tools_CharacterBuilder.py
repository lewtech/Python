import random



class PlayerCharacter(object):
    def __init__ (self, name, character_class):
        self.name = name
        self.character_class = character_class


def main():
    generate_abilities()
    gather_info()
    save_to_data()


def gather_info():
    print ("\n")
    name = input("What is thy character's name? ")
    gameclass = input("What path shall thou travel? ")

def roll(sides):
    roll = random.randint(1,sides)
    return roll

def roll4d6():
    cache = []
    sum = 0
    for i in range (0,4):
        roll_1d6 = roll(6)
        cache.append(roll_1d6)
        sum = sum + roll_1d6
    return sum-min(cache)


def roll_numdice_die(numdice,die):
    sum = 0
    for i in range (0,numdice):
        roll(die)
        sum = sum + roll(die)
    return sum



def generate_abilities():
    min_score = 13
    elite_score = 16
    ability_list = []
    print ("str dex con int wis cha")
    for i in range (0,8):
        classes = []
        for j in range (0,6):
            score = roll4d6()

            print (score, end = " ")

            if score >= min_score and j == 0:
                class_options = "fighter/barbarian"
                if score >= elite_score:
                    class_options = class_options.upper()
                classes.append (class_options)


            if score >= min_score and j == 1:
                class_options = "rogue/ranger"
                if score >= elite_score:
                    class_options = class_options.upper()
                classes.append (class_options)
            if score >= min_score and j == 3:
                class_options = "wizard"
                if score >= elite_score:
                    class_options = class_options.upper()
                classes.append(class_options)
            if score >= min_score and j == 4:
                class_options = "cleric/druid"
                if score >= elite_score:
                    class_options = class_options.upper()
                classes.append(class_options)
            if score >= min_score and j == 5:
                class_options = "sorcerer/bard"
                if score >= elite_score:
                    class_options = class_options.upper()
                classes.append(class_options)
        print (str(classes) + "\n")


def save_to_data():
    pass


main()






#lets use this as an exercise in parsing lists of lists
#rolls will be [[9,10,22,21,2,3]]