import random

class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.defense = 3
        self.health = 100
        self.block = False
        self.specialOn = False
    
    def show_stats( self ):
        print(f"Name: {self.name}\nClass: Ninja\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        self.block = False
        attack = random.randint(1,(5+pirate.speed))
        debuff = 0
        debuff += Ninja.check_defense(pirate.block, pirate.defense)
        debuff += Ninja.check_special(pirate.specialOn)
        if attack == 1:
            print(f"{self.name} throws a shuriken at {pirate.name}! {pirate.name} is hit and  takes {self.strength - debuff} damage!")
            pirate.health -= (self.strength - debuff)
        elif attack == 2:
            print(f"{self.name} slices with their katana! {pirate.name} is cut and takes {self.strength - debuff} damage!")
            pirate.health -= (self.strength - debuff)
        elif attack == 3:
            print(f"{self.name} karate chops {pirate.name}! {pirate.name} takes {self.strength - debuff} damage!")
            pirate.health -= (self.strength - debuff)
        elif attack == 4:
            print(f"{self.name} dazzles {pirate.name} with their firecrackers! {pirate.name} takes {self.strength - debuff} damage in the confusion!")
            pirate.health -= (self.strength - debuff)
        elif attack == 5:
            print(f"{self.name} tried to get too fancy and whiffed!")
        else:
            print(f"{self.name} attacks but {pirate.name} dodges the attack!")
        pirate.block = False
        pirate.specialOn = False
        return self

    def defend(self):
        print(f"{self.name} holds up their katana to block!")
        self.block = True

    def special(self):
        self.block = False
        print(f"{self.name} throws a smoke bomb and will avoid all damage on the next attack!")
        self.specialOn = True

    @staticmethod
    def check_defense(block, defense):
        if block:
            return defense
        else:
            return 0

    def check_special(special):
        if special:
            return -5
        else:
            return 0