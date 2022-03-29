class Agent():
    'the agent class'

    def __init__(self, color):
        self.color = color

    def maxi(self, boardX, alpha, beta, depth):
        # maximization function
        if(depth == 0):
            return evaluationFunction()
        terr = self.checkPass(boardX)
        if(terr > alpha):
            alpha = terr
        for x, y in self.promisingPoints(boardX, 'Black'):
            if(alpha >= beta):
                break
            eval = self.mini(self.childBoard(boardX, x, y, 'Black'), alpha, beta, depth-1)
            if(eval >= alpha):
                alpha = eval
        return alpha


    def mini(self, boardX, alpha, beta, depth):
        #minimization function
        if(depth == 0):
            return evaluationFunction()
        terr = self.checkPass(boardX)
        if(terr < beta):
            beta = terr
        for x, y in self.promisingPoints(boardX, 'White'):
            if(beta <= alpha):
                break
            eval = self.maxi(self.childBoard(boardX, x, y, 'White'), alpha, beta, depth-1)
            if(eval < beta):
                beta = eval
        return beta

    def nextMove(self, grid):
        # rerturn position of the Agent next move
        boardX = new Board(grid)
        alpha = self.checkPass(boardX)
        beta = 99999999
        depth = 7
        point = (-1, -1)
        for x, y in self.promisingPoints(boardX, 'Black'):
            eval = self.mini(self.childBoard(boardX, x, y, 'Black'), alpha, beta, depth-1)
            if(eval > alpha):
                alpha = eval
                point = (x, y)
        return point

    def checkPass(self, board):
        x, y = board.calculateTerritory()
        return x

    def evaluationFunction():
        # evaluation function for the leaves

    def promisingPoints(self, board, stoneCol):
        #return most promising points to the given player considaring the given boared
        pointsPow = self.pointspowers(board, stoneCol)
        return [y for x, y in pointsPow.sort(reverse=True)[:min(len(pointsPow), 20)]]

    def pointsPowers(self, board, stoneCol):
        # calculate the power for all empty points
        pointsPow = []
        stoneX = new Stone(stoneCol, (-1, -1))
        for x in range(9):
            for y in range(9):
                stoneX.position = (x, y)
                if(board[x][y] == None && board.legal(stoneX)):
                    pointsPow.append((self.singlePointPower(board, stoneX), (x, y)))
        return pointsPow

    def singlePointPower(self, board, stoneX):
        #calculate the power of a single empty point in the given board
        return self.PointDensity(stoneX, board) + self.checkPointStrategies(stoneX, board)

        '''
    def PointDensity(x, y):
        #claculate the density of an empty point
    def checkPointStrategies(x, y):
        # check if point apply any strategy
        '''

    def childBoard(self, board, x, y, stoneCol):
        # return the given board after putting given stone in x, y
        boardX = new Board(board.points)
        stoneX = new Stone(stoneCol, (x, y))
        boardX.placeOnBoard(stoneX)
        return boardX
