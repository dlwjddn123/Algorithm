from collections import deque
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = []
def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[y][x] = True
    sheep = 0
    wolf = 0
    if board[y][x] == 'v':
        wolf += 1
    elif board[y][x] == 'o':
        sheep += 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < C and 0 <= ny < R and not visited[ny][nx] and board[ny][nx] != "#":
                if board[ny][nx] == 'o':
                    sheep += 1
                elif board[ny][nx] == 'v':
                    wolf += 1
                visited[ny][nx] = True
                q.append([nx, ny])
    if wolf >= sheep:
        result.append([0, wolf])
        return 
    result.append([sheep, 0]) 


for i in range(R):
    for j in range(C):
        if not visited[i][j] and board[i][j] != '#':
            bfs(j, i)
s = 0
w = 0
for n in result:
    s += n[0]
    w += n[1]
print(f"{s} {w}")