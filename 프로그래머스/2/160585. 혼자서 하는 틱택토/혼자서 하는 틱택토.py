def validate(board, O, X):
    end = [[[i, 0], [i, 1], [i, 2]] for i in range(3)]
    end += [[[0, i], [1, i], [2, i]] for i in range(3)]
    end += [[[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]]
    winner = ""
    for case in end:
        if board[case[0][0]][case[0][1]] == 'O' and board[case[1][0]][case[1][1]] == 'O' and board[case[2][0]][case[2][1]] == 'O':
            winner += 'O'
                                                                                                
        elif board[case[0][0]][case[0][1]] == 'X' and board[case[1][0]][case[1][1]] == 'X' and board[case[2][0]][case[2][1]] == 'X':
            winner += 'X'                                                                                                   
    if winner == 'O' and O == X:
        return False
    if winner == 'X' and O > X:
        return False
    if winner == 'OO' and X == 4:
        return True
    return len(winner) < 2

def OXCount(board):
    O = 0
    X = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                X += 1
            elif board[i][j] == 'O':
                O += 1
    return [O, X]

def solution(board):
    answer = -1
    O, X = OXCount(board)
    if abs(O - X) >= 2 or O - X < 0:
        return 0
    if validate(board, O, X):
        return 1
    return 0


    
    