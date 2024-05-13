from collections import deque

points = [
    [[-1, -1], [-1, 0], [0, -1]], 
    [[-1, 0], [-1, 1], [0, 1]], 
    [[0, -1], [1, -1], [1, 0]],
    [[0, 1], [1, 0], [1, 1]]]

def solution(m, n, board):
    for i in range(len(board)):
        board[i] = list(board[i])
    answer = 0
    while True:
        if not go(board):
            break
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "":
                answer += 1
    return answer

def go(board):
    removePoints = []
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != "":
                find4Blocks(i, j, board, removePoints)
                            
    for y, x in removePoints:
        board[y][x] = ""
    # for n in board:
    #     print(n)
    # print()
    downBlocks(board)
    # for n in board:
    #     print(n)
    # print()
    return len(removePoints) != 0
                            
def downBlocks(board):
    downPoints = [0 for _ in range(len(board[0]))]
    startPoints = [0 for _ in range(len(board[0]))]
    
    for i in range(len(board[0])):
        for j in range(len(board)-1, -1, -1):
            if board[j][i] == "":
                downPoints[i] = j
                break
        for j in range(downPoints[i], -1, -1):
            if board[j][i] != "":
                startPoints[i] = j
                break
                
    for i in range(len(board[0])):
        for j in range(startPoints[i], -1, -1):
            if board[j][i] != "" and downPoints[i] > j:
                board[downPoints[i]][i] = board[j][i]
                board[j][i] = ""
                downPoints[i] -= 1                
    
def find4Blocks(y, x, board, removePoints):
    friend = board[y][x]
    N, M = len(board), len(board[0])
    for point in points:
        nx1, nx2, nx3 = x + point[0][1], x + point[1][1], x + point[2][1]    
        ny1, ny2, ny3 = y + point[0][0], y + point[1][0], y + point[2][0]
        if 0 <= nx1 < M and 0 <= ny1 < N and 0 <= nx2 < M and 0 <= ny2 < N and 0 <= nx3 < M and 0 <= ny3 < N and board[ny1][nx1] == friend and board[ny2][nx2] == friend and board[ny3][nx3] == friend:
            removePoints.append([ny1, nx1])
            removePoints.append([ny2, nx2])
            removePoints.append([ny3, nx3])
            removePoints.append([y, x])

            
    