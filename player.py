from game import *

class Player:
    def __init__(self, game, piece):
        self.piece = piece
        self.game = game

    def placePiece(self, row, col):
        '''
        Place the piece in the position.
        '''
        self.game.board[row][col] = self.piece

    def getMove(self):
        pass

class Human(Player):
    def __init__(self, game, piece):
        super().__init__(game, piece)

    def __canParseInt(self, x):
        '''
        Check if x can be parsed to int.
        '''
        try:
            int(x)
            return True
        except:
            return False

    def __getRow(self):
        '''
        Get the input for row.
        '''
        row = input('Row: ')
        while not self.__canParseInt(row):
            print('Integer input ONLY')
            row = input('Row: ')
        return int(row) - 1

    def __getCol(self):
        '''
        Get the input for column.
        '''
        col = input('Col: ')
        while not self.__canParseInt(col):
            print('Integer input ONLY')
            col = input('Col: ')
        return int(col) - 1

    def getMove(self):
        '''
        Get the input for position to place piece.
        '''
        row = self.__getRow()
        col = self.__getCol()
        while row > 2 or row < 0 or col > 2 or col < 0 or not self.game.isSpotEmpty(row, col):
            print('This spot is occupied or invalid. Try another one.')
            row = self.__getRow()
            col = self.__getCol()
        return row, col

class MinimaxPlayer(Player):
    def __init__(self, game, piece):
        super().__init__(game, piece)
        if self.piece == PIECE_X:
            self.opponentPiece = PIECE_O
        else:
            self.opponentPiece = PIECE_X

    def getMove(self):
        '''
        Get the best position to place piece using minimax with alpha-beta pruning.
        '''
        best = -99999
        alpha, beta = -99999, 99999
        if self.piece == PIECE_O:
            best = 99999
        for row, col in self.game.getEmptySpot():
            self.game.board[row][col] = self.piece
            temp = self.__minimax(self.opponentPiece, alpha, beta)
            if self.piece == PIECE_X and temp > best or self.piece == PIECE_O and temp < best:
                best = temp
                move = (row, col)
            self.game.board[row][col] = EMPTY
        return move

    def __minimax(self, piece, alpha, beta):
        if self.game.isOver():
            return self.game.score()
        if piece == PIECE_X:
            return self.__maxVal(piece, alpha, beta)
        else:
            return self.__minVal(piece, alpha, beta)

    def __maxVal(self, piece, alpha, beta):
        val = -99999
        for row, col in self.game.getEmptySpot():
            self.game.board[row][col] = piece
            val = max(val, self.__minimax(PIECE_O, alpha, beta))
            self.game.board[row][col] = EMPTY
            if val > beta:
                return val
            alpha = max(alpha, val)
        return val

    def __minVal(self, piece, alpha, beta):
        val = 99999
        for row, col in self.game.getEmptySpot():
            self.game.board[row][col] = piece
            val = min(val, self.__minimax(PIECE_X, alpha, beta))
            self.game.board[row][col] = EMPTY
            if val < alpha:
                return val
            beta = min(beta, val)
        return val
