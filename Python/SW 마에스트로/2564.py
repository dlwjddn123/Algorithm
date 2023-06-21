from collections import deque
N, M = map(int, input().split())
C = int(input())
store = [list(map(int, input().split())) for _ in range(C+1)]
area = [[0]*(N+1) for _ in range(M+1)]
startX = 0
startY = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(M+1):
    if i != 0 and i != M:
        area[i][0], area[i][N] = 1, 1
        continue
    for j in range(N+1):
        if i == 0:
            area[i][j] = 1
        if i == M:
            area[i][j] = 1
        
for i in range(C+1):
    direct, distance = store[i][0], store[i][1]
    if direct == 1:
        if i == C:
            startX = distance
            startY = 0
            continue    
        area[0][distance] = 2
    elif direct == 3:
        if i == C:
            startX = 0
            startY = distance
            continue
        area[distance][0] = 2
    elif direct == 2:
        if i == C:
            startX = distance
            startY = M
            continue
        area[M][distance] = 2
    else:
        if i == C:
            startX = N
            startY = distance
            continue
        area[distance][N] = 2
visited = [[False]*(N+1) for _ in range(M+1)]

result = 0
def bfs(x, y):
    global result
    q = deque()
    q.append([x, y, 0])
    while q:
        x, y, count= q.popleft()
        count += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx <= N and 0 <= ny <= M and (area[ny][nx] == 1 or area[ny][nx] == 2) and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append([nx, ny, count])
                if area[ny][nx] == 2:
                    result += count

visited[startY][startX] = True
bfs(startX, startY)
print(result)
            

    
