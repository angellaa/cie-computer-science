board = [['B' for i in range(8)] for i in range(2)] + \
        [['E' for i in range(8)] for i in range(4)] + \
        [['W' for i in range(8)] for i in range(2)]

# board = [['b' for i in range(8)] for i in range(2)]

# for i in range(4):
#    board.append(['e' for i in range(8)])

# for i in range(2):
#    board.append(['w' for i in range(8)])

board[3][1] = 'W'
board[3][3] = 'B'
board[3][7] = 'B'

print(board)

def ValidMoves(pieceColour, xCurrent, yCurrent):
    if pieceColour == 'B':
        g = 'W'
    else:
        g = 'B'
    print('possible moves left are')

    for i in range(xCurrent, -1, -1):
        if board[yCurrent][i] == 'E':
            print('{} {}'.format(i, yCurrent))
        if board[yCurrent][i] == g:
            print('{} {} REMOVE piece'.format(i, yCurrent))
        break


ValidMoves('B', 3, 3)