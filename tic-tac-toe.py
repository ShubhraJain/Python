board = [' ']*9

keyMap = {
'tL':0,
'tM':1,
'tR':2, 
'mL':3,
'mM':4,
'mR':5,
'bL':6,
'bM':7,
'bR':8 
}

def hasWon(board, turn):
    # return true if the board has been won by the char entered (either 'X' or '0')
    # check each row, each column and each diagonal
    target = [turn] * 3
    return ((board[0:3] == target)
     or (board[3:6] == target)
     or (board[6:9] == target)
     or (board[0:9:3] == target) 
     or (board[1:9:3] == target)
     or (board[2:9:3] == target)
     or (board[0:9:4] == target)
     or (board[2:8:2] == target))

def hasEmpty(board):
    # check if there is any empty space where anything can be entered
    return ' ' in board


def print_board(board):
    print(' | '.join(board[0:3]))
    print('*********')
    print(' | '.join(board[3:6]))
    print('*********')
    print(' | '.join(board[6:9]))

turn = 'X'
for i in range(9):
    print(turn + "\'s turn. Which space do you wanna move?:")
    move = keyMap[input()]
    
    if board[move] == ' ':
        board[move] = turn
    else:
        print("This space has already been chosen. \nChoose other space")
        move = keyMap[input()]
        board[move] = turn
    print_board(board)
    
    if hasWon(board, turn):
        print(turn, " has won")
        break
    elif not hasEmpty(board):
        print("It's a tie")
        break

    # if control comes here, it means move is possible.
    # flip the turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    print("turn:" + turn)
