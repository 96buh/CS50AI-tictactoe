"""
Tic Tac Toe Player
"""

import math
<<<<<<< HEAD

=======
import copy
>>>>>>> 7cc95f1f0dfbf7140ddf29833bb29e351e113161
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
<<<<<<< HEAD
    raise NotImplementedError
=======
    X_num = 0   
    O_num = 0
    for i in range(3):    
        for j in range(3):
            if board[i][j] == X:
                X_num += 1
            if board[i][j] == O:
                O_num +=1
    if X_num > O_num:
        return O
    else:
        return X
        
    
>>>>>>> 7cc95f1f0dfbf7140ddf29833bb29e351e113161


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
<<<<<<< HEAD
    raise NotImplementedError

=======
    legal_move = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                legal_move.add((i, j))
    return legal_move
>>>>>>> 7cc95f1f0dfbf7140ddf29833bb29e351e113161

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
<<<<<<< HEAD
    raise NotImplementedError
=======
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Action is not valid!")
    
    copy_board = copy.deepcopy(board)
    copy_board[action[0]][action[1]] = player(board)
    return copy_board
>>>>>>> 7cc95f1f0dfbf7140ddf29833bb29e351e113161


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
<<<<<<< HEAD
    raise NotImplementedError
=======
    # 檢查row
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return board[i][0]
    # 檢查col
    for j in range(3):
        if board[0][j] == board[1][j] and board[0][j] == board[2][j]:
            return board[0][j]
    # 檢查對角線
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[0][2]

    return None

>>>>>>> 7cc95f1f0dfbf7140ddf29833bb29e351e113161


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
<<<<<<< HEAD
    raise NotImplementedError
=======
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return False
    return True
    
>>>>>>> 7cc95f1f0dfbf7140ddf29833bb29e351e113161


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
<<<<<<< HEAD
    raise NotImplementedError
=======
    if terminal(board):
        if winner(board) == X:
            return 1
        if winner(board) == O:
            return -1
        else:
            return 0
>>>>>>> 7cc95f1f0dfbf7140ddf29833bb29e351e113161


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
<<<<<<< HEAD
    raise NotImplementedError
=======
    if terminal(board):
        return None
>>>>>>> 7cc95f1f0dfbf7140ddf29833bb29e351e113161
