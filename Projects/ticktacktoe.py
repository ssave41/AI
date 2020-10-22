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
    num_of_x = 0
    num_of_o = 0

    # calculate the quantity of X and O
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                num_of_x += 1
            elif board[i][j] == O:
                num_of_o += 1

    if num_of_x > num_of_o:
        return(O)
    else:
        return(X)


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    
    return(actions)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    move = player(board)
    if new_board[action[0]][action[1]] == EMPTY:
        new_board[action[0]][action[1]] = move
        return(new_board)
    else:
        raise NameError('Not valid action')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                #check diagonals
                if i == 0 and j == 0:
                    if board[i][j] == board[i+1][j+1] == board[i+2][j+2]:
                        return(board[i][j])
                
                if i == 0 and j == 2:
                    if board[i][j] == board[i+1][j-1] == board[i+2][j-2]:
                       return(board[i][j])
                #check horizontal rows
                try:
                    if board[i][j] == board[i][j+1] == board[i][j+2]:
                        return(board[i][j])

                except IndexError:
                    pass
                #check vertical rows     
                try:
                    if board[i][j] == board[i+1][j] == board[i+2][j]:
                        return(board[i][j])     
                except IndexError:
                    pass
    return(None)   


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    return(False)
    return(True)




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    tmp = winner(board)
    if tmp == X:
        return(1)
    elif tmp == O:
        return(-1)
    else:
        return(0)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    def min_value(board):
        v = 2
        if terminal(board):
            return(utility(board))
        
        for move in actions(board):
            v = min(v, max_value(result(board, move)))
            if v == -1:
                break
        
        return v

    def max_value(board):
        v = -2
        if terminal(board):
            return(utility(board))
        
        for move in actions(board):
            v = max(v, min_value(result(board, move)))
            if v == 1:
                break
        
        return v


    if terminal(board):
        return None 

    moves = actions(board)
    
    if player(board) == X:
        for move in moves:
            if min_value(result(board, move)) == 1:
                return move
        for move in moves:    
            if min_value(result(board, move)) == 0:
                return move

    elif player(board) == O:
        for move in moves:
            if max_value(result(board, move)) == -1:
                return move
        for move in moves:    
            if max_value(result(board, move)) == 0:
                return move
