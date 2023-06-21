from collections import deque
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
sharkPos = [0, 0]
sharkSize = 2
ateFishCount = 0
time = 0
momCall = True
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            sharkPos[0] = j
            sharkPos[1] = i
            break

def bfs(x1, y1):
    global sharkSize, time, ateFishCount
    q = deque()
    q.append([x1, y1, 0])
    visited[y1][x1] = True
    fishPos = []
    t = 100000000
    chk = False
    while q:
        x, y, timeCount = q.popleft()
        timeCount += 1
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < N and board[ny][nx] <= sharkSize and not visited[ny][nx]:
                visited[ny][nx] = True
                if board[ny][nx] == 0 or board[ny][nx] == sharkSize:
                    q.append([nx, ny, timeCount])
                elif board[ny][nx] < sharkSize and t >= timeCount:
                    if t == timeCount:
                        fishPos.append([nx, ny])
                    else:
                        t = timeCount
                        fishPos = [[nx, ny]]
    if len(fishPos) == 0:
        return False
    else:
        fishPos.sort(key=lambda x : (x[1], [0]))
        sharkPos[0], sharkPos[1] = fishPos[0][0], fishPos[0][1]
        board[y1][x1], board[sharkPos[1]][sharkPos[0]] = 0, 9
        ateFishCount += 1
        time += t
        if ateFishCount == sharkSize:
            sharkSize += 1
            ateFishCount = 0
        return True
while momCall:
    visited = [[False]*N for _ in range(N)]
    momCall = bfs(sharkPos[0], sharkPos[1])
print(time)
                    
