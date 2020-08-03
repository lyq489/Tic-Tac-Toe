EMPTY = 0
PIECE_X = 1
PIECE_O = 2
CONNCECT_GOAL = 3
BOARD_SIZE = 3

class Game:
    def __init__(self, board):
        self.board = board

    def score(self):
        '''
        Return 1 if X wins, -1 if O wins, 0 if a tie occurs.
        '''
        # horizontal
        for row in range(len(self.board)):
            for col in range(len(self.board) - CONNCECT_GOAL + 1):
                if self.board[row][col] != EMPTY and self.board[row][col] == \
                    self.board[row][col + 1] == self.board[row][col + 2]:
                    if self.board[row][col] == PIECE_X:
                        return 1
                    else:
                        return -1
        # vertical
        for row in range(len(self.board) - CONNCECT_GOAL + 1):
            for col in range(len(self.board)):
                if self.board[row][col] != EMPTY and self.board[row][col] == \
                    self.board[row + 1][col] == self.board[row + 2][col]:
                    if self.board[row][col] == PIECE_X:
                        return 1
                    else:
                        return -1
        # diagonal ascending
        for row in range(CONNCECT_GOAL - 1, len(self.board)):
            for col in range(len(self.board)  - CONNCECT_GOAL + 1):
                if self.board[row][col] != EMPTY and self.board[row][col] == \
                    self.board[row - 1][col + 1] == self.board[row - 2][col + 2]:
                    if self.board[row][col] == PIECE_X:
                        return 1
                    else:
                        return -1
        # diagonal descending
        for row in range(len(self.board)  - CONNCECT_GOAL + 1):
            for col in range(len(self.board)  - CONNCECT_GOAL + 1):
                if self.board[row][col] != EMPTY and self.board[row][col] == \
                    self.board[row + 1][col + 1] == self.board[row + 2][col + 2]:
                    if self.board[row][col] == PIECE_X:
                        return 1
                    else:
                        return -1
        # tie
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == EMPTY:
                    # game still going on
                    return None
        return 0

    def isOver(self):
        '''
        Check if game is over.
        '''
        return self.score() != None

    def isSpotEmpty(self, row, col):
        '''
        Check if the spot is empty, so a piece can be placed there.
        '''
        return self.board[row][col] == 0

    def getEmptySpot(self):
        '''
        Return a list of empty spot coordinates.
        '''
        empty = []
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == 0:
                    empty.append((row, col))
        return empty

    def printMessage(self):
        '''
        Print the result of game.
        '''
        if self.score() == None:
            #game still going on no message needed
            return
        elif self.score() == 1:
            print('X wins!')
        elif self.score() == -1:
            print('O wins!')
        elif self.score() == 0:
            print('Game ends up with a tie!')

    def __str__(self):
        '''
        Sample board:
        -------------
        | x | o | o |
        -------------
        | o | x | x |
        -------------
        | x | x | o |
        -------------
        '''
        lines = []
        rowLine = '   '
        for i in range(len(self.board)):
            if i < 10:
                rowLine += '  ' + str(i + 1) + ' '
            elif i == 10:
                rowLine += ' ' + str(i + 1) + '  '
            else:
                rowLine += str(i + 1) + '  '
        lines.append(rowLine)
        horizontalLine = '   ' + '-' * (1 + len(self.board) * 4)
        lines.append(horizontalLine)
        i = 1
        for row in self.board:
            if i < 10:
                rowLine = ' ' + str(i) + ' |'
            else:
                rowLine = str(i) + ' |'
            for col in row:
                if col == PIECE_X:
                    rowLine += ' x |'
                elif col == PIECE_O:
                    rowLine += ' o |'
                else:
                    rowLine += '   |'
            lines.append(rowLine)
            lines.append(horizontalLine)
            i += 1
        return '\n'.join(lines)