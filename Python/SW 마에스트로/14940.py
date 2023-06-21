from collections import deque

n, m = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
blocked = False

def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and Map[ny][nx] != 0:
                if blocked:
                    Map[ny][nx] = -1
                else:
                    if [a, b] != [startX, startY]:
                        Map[ny][nx] = Map[b][a] + 1
                visited[ny][nx] = True
                q.append([nx, ny])
                
for i in range(n):
    for j in range(m):
        if Map[i][j] == 2:
            startX = j
            startY = i
Map[startY][startX] = 0
bfs(startX, startY)        
blocked = True

for i in range(n):
    for j in range(m):
        if not visited[i][j] and Map[i][j] == 1:
            Map[i][j] = -1
            bfs(j, i)

for n in Map:
    print(*n)

            

    