def makeMove():
        valid_move = False

        move = input("What would you like to do? (attack / defend / special): ")
        while valid_move == False:
            if move.lower() == 'attack' or move.lower() == 'defend' or move.lower() == 'special':
                valid_move = True
                return move
            else:
                move = input("Please make a valid move (attack / defend / special): ")

def checkWin(ninja, pirate):
    if ninja.health <= 0:
        print(f"{pirate.name} defeats {ninja.name}! Pirates win!")
    elif pirate.health <= 0:
        print(f"{ninja.name} defeats {pirate.name}! Ninjas win!")