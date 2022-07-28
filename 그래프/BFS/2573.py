from collections import deque


N, M = map(int, input().split())
Map = []
for _ in range(N):
    n = list(map(int, input().split()))
    Map.append(n)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    global Map, visited
    q = deque([x, y])
    visited = [[False]*M for _ in range(N)]
    while q:
        count = 0
        nx = q.popleft()
        ny = q.popleft()
        visited[ny][nx] = True
        for i in range(4):
            if 0 <= nx + dx[i] <= M-1 and 0 <= ny + dy[i] <= N-1:
                if Map[ny+dy[i]][nx+dx[i]] == 0 and not visited[ny+dy[i]][nx+dx[i]]:
                    count += 1
                    continue
                if Map[ny+dy[i]][nx+dx[i]] != 0 and not visited[ny+dy[i]][nx+dx[i]]:
                    visited[ny+dy[i]][nx+dx[i]] = True
                    q.append(nx+dx[i])
                    q.append(ny+dy[i])
        Map[ny][nx] = Map[ny][nx] - count
        if Map[ny][nx] < 0 :
            Map[ny][nx] = 0
year = 0
while True:
    check = False
    visited = [[False]*M for _ in range(N)]
    count = 0 
    for i in range(N):
        for j in range(M):
            if Map[i][j] != 0 and not visited[i][j]:
                count += 1
                check = True
                bfs(j, i)
    if count >= 2:
        print(year)
        break
    year += 1
    if not check:
        print(0)
        break




                    