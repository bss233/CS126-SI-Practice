from random import randint

class Wizard:

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.spellbook = []
        self.xpEarned = 0
        self.xpToLevel = 15
        self.hp = randint(6, 13)
        self.maxHp = self.hp
        self.alive = True


    #######     Spellbook     #######
    def displaySpellbook(self):
        for spell in spellbook:
            print(spell)
    
    def addSpell(self, spell):
        self.spellbook.append(spell)
    ################################

    ########     Name     #######
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
    ################################

    ########     Hp     ############
    def getHp(self):
        return self.hp
    
    def _setHp(self, hp):
        self.hp = hp

    def heal(self, increaseBy):
        hp = self.getHp + increasedBy
        self._setHp(hp)

    def takeDamage(self, reduceBy):
        hp = self.getHp + reduceBy
        self._setHp(hp)
    ################################
    
    #######      Alive     #########
    def getAlive(self):
        return self.alive

    def setAlive(self, status):
        self.alive = status

    def isDead(self):
        if self.getHP() <= 0:
            self.setAlive(False)
    ################################
            
    #######      XP      ###########
    def getXpEarned(self):
        return self.xpEarned

    def getXpToLevel(self):
        return self.xpToLevel
    
    def setXpEarned(self, amount):
        self.xpEarned = amount

    def setXpToLevel(self, amount):
        self.xpToLevel = amount
    ################################

    #######     Level      #########
    def getLevel(self):
        return self.level

    def setLevel(self, level):
        self.level = level
    ################################
    
