from collections import deque
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

chk = True

def bfs(x, y):
    q = deque()
    q.append([x, y])
    board[y][x] = -1
    visited[y][x] = True
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[ny][nx]:
                visited[ny][nx] = True
                if board[ny][nx] == 0:
                    board[ny][nx] = -1
                    q.append([nx, ny])
                if board[ny][nx] == 1:
                    board[ny][nx] = 0
                    count += 1

    for n in board:
        print(n)
    print()
    return count
day = 0
cheese = 0
while chk:
    chk = False
    day += 1
    visited = [[False]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if not visited[i][j] and board[i][j] == 0:
                chk = True
                cheese = bfs(j, i)
print(day)
print(cheese)