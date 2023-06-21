from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1 ,1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    global board
    copyBoard = []
    for i in range(N):
        copyBoard.append(board[i][::])
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
                visited[ny][nx] = True
                if copyBoard[ny][nx] == 0:
                    copyBoard[ny][nx] = -1
                    q.append([nx, ny])
    def go():
        for i in range(N):
            for j in range(M):
                count = 0
                if board[i][j] == 1:
                    for k in range(4):
                        nx1, ny1 = j + dx[k], i + dy[k]
                        if 0 <= nx1 < M and 0 <= ny1 < N and copyBoard[ny1][nx1] == -1:
                            count += 1
                            if count == 2:
                                break
                if count == 2:
                    board[i][j] = 0
    go()
day = 0
chk = 0
for i in range(N):
    chk += sum(board[i])
if chk == 0:
    print(0)
else:
    while True:              
        day += 1     
        visited = [[False]*M for _ in range(N)]
        check = 0
        bfs(0, 0)
                    
        for i in range(N):
            check += sum(board[i])

        if check == 0:
            break          
    print(day)



