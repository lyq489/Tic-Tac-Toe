from game import *
from player import *

if __name__ == '__main__':
    board = [[EMPTY for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
    game = Game(board)
    print('Initial Board')
    print(game)
    # alternatively AI against AI or Human against Human
    player1 = Human(game, PIECE_X)
    player2 = MinimaxPlayer(game, PIECE_O)

    while not game.isOver():
        row, col = player1.getMove()
        player1.placePiece(row, col)
        print(game)
        game.printMessage()
        if not game.isOver():
            row, col = player2.getMove()
            player2.placePiece(row, col)
            print(game)
            game.printMessage()
