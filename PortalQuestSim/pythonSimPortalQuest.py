class Hero(object):
    def __init__(self, name, attack, speed, maxHealth, energyGain):
        self.name = name
        self.attack = attack
        self.speed = speed
        self.maxHealth = maxHealth
        self.health = maxHealth
        self.energyGain = energyGain
        self.dps = attack/speed
        self.energy = 0
        self.abilityWhite = "burst"
        self.abilityWhiteAmount1 = 1000
        self.abilityWhiteAmount2 = 1202
        self.abilityGreen = "splashOnHit"
        self.abilityGreenAmount1 = 1603
        self.abilityBlue = "saved"
        self.abilityPurple = "armor"
        
        

        

        
        
shieldMaiden = Hero("shieldMaiden", 2490, .39, 78328,11)
shieldMaidenEnemy = Hero("shieldMaiden", 2490, .39, 78328,11)

counter = 0
dps = shieldMaiden.attack/.39

while shieldMaiden.health > 0:
    #gameloop
    shieldMaiden.health = shieldMaiden.health- shieldMaiden.dps
    counter = counter +1
    
    shieldMaiden.energy = shieldMaiden.energy + shieldMaiden.energyGain
    if shieldMaiden.energy > 100:
        #fire white ability
        shieldMaiden.energy = 0
        print ("****White Ability****")
        shieldMaiden.health = shieldMaiden.health - shieldMaiden.abilityWhiteAmount1
        
    print (str(counter) + " seconds, enemy does " + str(shieldMaiden.dps) + " points of damage") 
    print (shieldMaiden.health)

print ("shieldMaiden is dead")


