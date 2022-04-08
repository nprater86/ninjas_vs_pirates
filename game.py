from classes.ninja import Ninja
from classes.pirate import Pirate
from functions import *

import random

class_choice_valid = False
class_choice = input('What class would you like to be?: Ninja or Pirate? \n')

while class_choice_valid == False:
    if class_choice.lower() == 'ninja':
        name = input("What is your ninja's name?: ")
        ninja = Ninja(name)
        pirate = Pirate('Jack Sparrow')
        class_choice_valid = True
    elif class_choice.lower() == 'pirate':
        name = input("What is your pirate's name?: ")
        pirate = Pirate(name)
        ninja = Ninja('Sekiro')
        class_choice_valid = True
    else:
        class_choice = input("Please pick a valid class: Ninja or Pirate? \n")

if class_choice.lower() == 'ninja':
    while ninja.health > 0 and pirate.health > 0:
        print(f"{ninja.name}'s Health: {ninja.health}")
        print(f"{pirate.name}'s Health: {pirate.health}")
        valid_move = False

        move = makeMove()
        
        if move.lower() == 'attack':
            ninja.attack(pirate)
        elif move.lower() == 'defend':
            ninja.defend()
        elif move.lower() == 'special':
            ninja.special()

        pirateMove = random.randint(1,3)
        if pirateMove == 1:
            pirate.attack(ninja)
        if pirateMove == 2:
            pirate.defend()
        if pirateMove == 3:
            pirate.special()

        checkWin(ninja, pirate)

elif class_choice.lower() == 'pirate':
    while ninja.health > 0 and pirate.health > 0:
        print(f"{ninja.name}'s Health: {ninja.health}")
        print(f"{pirate.name}'s Health: {pirate.health}")

        move = makeMove()

        ninjaMove = random.randint(1,3)
        if ninjaMove == 1:
            ninja.attack(pirate)
        if ninjaMove == 2:
            pirate.defend()
        if ninjaMove == 3:
            pirate.special()

        if move.lower() == 'attack':
            pirate.attack(ninja)
        elif move.lower() == 'defend':
            pirate.defend()
        elif move.lower() == 'special':
            pirate.special()

        checkWin(ninja, pirate)