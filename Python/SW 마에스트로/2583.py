from collections import deque

M, N, K = map(int, input().split())
area = [[0]*(N) for _ in range(M)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = []

def fillArea(x1, y1, x2, y2):
    for i in range(y1, y2):
        for j in range(x1, x2):
            area[i][j] = 1

def bfs(startX, startY):
    q = deque()
    q.append([startX, startY])
    area[startY][startX] = 1
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and area[ny][nx] == 0:
                area[ny][nx] = 1
                count += 1
                q.append([nx, ny])
    result.append(count)

for _ in range(K):
    LDx, LDy, RUx, RUy = map(int, input().split())
    fillArea(LDx, LDy, RUx, RUy)

for i in range(M):
    for j in range(N):
        if area[i][j] == 0:
            bfs(j, i)
print(len(result))
print(*sorted(result))