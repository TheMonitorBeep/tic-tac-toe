"""
Tic Tac Toe Player
"""

import math
import copy

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
    p = 0
    z=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
                p = p+1
            elif board[i][j]==O:
                z = z+1
    if p==z:
        return X
    else:
        return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==None:
                action.add((i,j))
    return action


    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]]!=None:
        raise ValueError("Action Invalid")
    else:
        b = copy.deepcopy(board)
        b[action[0]][action[1]] = player(b)
        return b


    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #horizontally
    for i in board:
        if i==[X,X,X]:
            return X
        elif i==[O,O,O]:
            return O
    #vertically
    for j in range(3):
        r = []
        for k in range(3):
            r.append(board[k][j])
        if r==[X,X,X]:
            return X
        elif r==[O,O,O]:
            return O
    #diagonals
    s = [board[0][0],board[1][1],board[2][2]]
    t = [board[0][2],board[1][1],board[2][0]]
    if s==[X,X,X] or t==[X,X,X]:
        return X
    elif s==[O,O,O] or t==[O,O,O]:
        return O

    return None


    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j]==None:
                    return False
        return True


    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board)==X:
        y = MAX(board)
        for i in actions(board):
            if MIN(result(board,i))==y:
                return i
    elif player(board)==O:
        y =  MIN(board)
        for i in actions(board):
            if MAX(result(board,i))==y:
                return i


def MAX(board):
    if terminal(board):
        return utility(board)
    else:
        c = -1000
        for i in actions(board):
            c = max(c, MIN(result(board, i)))
        return c

def MIN(board):
    if terminal(board):
        return utility(board)
    else:
        c = 1000
        for i in actions(board):
            c = min(c, MAX(result(board,i)))
        return c