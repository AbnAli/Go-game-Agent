class Opponent:
    'this class represents the human player'

    stoneColor

    def __init__(self, stoneColor):
        #intialize the opponent color
        Opponent.stoneColor = stoneColor


    def nextMove(self):
        # get the move of the human player
        stone = new Stone(Opponent.stoneColor, (-1, -1), False);
        choice = input("Enter 'C' to set a move or 'P' to pass: ")
        if(choice == 'P' || choice == 'p'):
            return (-1, -1)
        x, y = input("Enter the coordinate of your move: ")
        stone.position = (x, y)
        return stone
