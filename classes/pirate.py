import random

class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.defense = 5
        self.health = 100
        self.block = False
        self.specialOn = False

    def show_stats( self ):
        print(f"Name: {self.name}\nClass:Pirate\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        self.block = False
        attack = random.randint(1,(5+ninja.speed))
        debuff = 0
        debuff += Pirate.check_defense(ninja.block, ninja.defense)
        debuff += Pirate.check_special(ninja.specialOn, self.strength)
        if attack == 1:
            print(f"{self.name} fires their hand cannon! {ninja.name} is hit and  takes {self.strength - debuff} damage!")
            ninja.health -= (self.strength - debuff)
        elif attack == 2:
            print(f"{self.name} swings their sword! {ninja.name} gets sliced and takes {self.strength - debuff} damage!")
            ninja.health -= (self.strength - debuff)
        elif attack == 3:
            print(f"{self.name} sends their parrot after {ninja.name}! The parrot pecks at {ninja.name}, who takes {self.strength - debuff} damage!")
            ninja.health -= (self.strength - debuff)
        elif attack == 4:
            print(f"{self.name} kicks {ninja.name} with their peg leg! {ninja.name} takes {self.strength - debuff} damage!")
            ninja.health -= (self.strength - debuff)
        elif attack == 5:
            print(f"{self.name} is too drunk and misses!")
        else:
            print(f"{self.name} attacks but {ninja.name} dodges the attack!")
        ninja.block = False
        ninja.specialOn = False
        return self

    def defend( self ):
        print(f"{self.name} throws up their swashbuckler to defend themselves!")
        self.block = True

    def special(self):
        self.block = False
        if (100 - self.health) >= 10:
            print(f"{self.name} takes a long draw from his rum bottle and recovers 10 health but will take additional 5 damage on the next turn!")
            self.health += 10
            self.specialOn = True
        else:
            print(f"{self.name} takes a long draw from his rum bottle and recovers {100-self.health} health but will take additional 5 damage on the next turn!")
            self.health += 100-self.health
            self.specialOn = True

    @staticmethod
    def check_defense(block, defense):
        if block:
            return defense
        else:
            return 0

    @staticmethod
    def check_special(special, modifier):
        if special:
            return modifier
        else:
            return 0
