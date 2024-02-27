import copy

R, C, M = map(int, input().split())
board = [[None]*(C+1) for _ in range(R+1)]
dx = [0, 0, 0, 1, -1]
dy = [0, -1, 1, 0, 0]
result = 0

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r][c] = [s, d, z]

def fishing(col):
    global result
    for i in range(1, R+1):
        if board[i][col] != None:
            result += board[i][col][2]
            board[i][col] = None
            return

def moving():
    for i in range(1, R+1):
        for j in range(1, C+1):
            if board[i][j] != None :
                go(j, i, board[i][j][0], board[i][j][1])
    
def go(x, y, s, d):
    ny = y
    nx = x
    if d == 1 or d == 2:
        while s > 0:
            ny = ny + dy[d]
            if 0 < ny <= R:
                s -= 1
                continue
            if d == 1:
                d = 2
                ny = ny + dy[d] * 2
                s -= 1
                continue
            if d == 2:
                d = 1
                ny = ny + dy[d] * 2
                s -= 1
            
    elif d == 3 or d == 4:
        while s > 0:
            nx = nx + dx[d]
            if 0 < nx <= C:
                s -= 1
                continue
            if d == 3:
                d = 4
                nx = nx + dx[d] * 2
                s -= 1
                continue
            if d == 4:
                d = 3
                nx = nx + dx[d] * 2
                s -= 1
    if newBoard[ny][nx] == None:
        newBoard[ny][nx] = board[y][x]
        newBoard[ny][nx][1] = d
        return
    if newBoard[ny][nx][2] < board[y][x][2]:
        newBoard[ny][nx] = board[y][x]
        newBoard[ny][nx][1] = d

for i in range(1, C+1):
    newBoard = [[None]*(C+1) for _ in range(R+1)]
    fishing(i)
    moving()
    board = copy.deepcopy(newBoard)
print(result)