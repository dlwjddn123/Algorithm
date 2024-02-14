from collections import deque
import copy


N, M = map(int, input().split())
arr = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(N):
    n = list(map(int, input().split()))
    arr.append(n)

result = 0

def go():
    global result
    g = copy.deepcopy(arr)
    count = 0
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if g[i][j] == 2 and not visited[i][j]:
                bfs(g, j, i, visited)

    for i in range(N):
        for j in range(M):  
            if g[i][j] == 0 :
                count += 1
    
    if result < count:
        result = count
    

def bfs(g, x, y, visited):
    q = deque([x, y])
    visited[y][x] = True
    while q:
        nx = q.popleft()
        ny = q.popleft()
        for i in range(4):
            if 0 <= nx + dx[i] <= M-1 and 0 <= ny + dy[i] <= N-1:
                if not visited[ny+dy[i]][nx+dx[i]] and g[ny+dy[i]][nx+dx[i]] == 0 :
                    visited[ny+dy[i]][nx+dx[i]] = True
                    g[ny+dy[i]][nx+dx[i]] = 2
                    q.append(nx+dx[i])
                    q.append(ny+dy[i])
        

                    
def makeWall(cnt):
    if cnt == 3:
        go()
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                makeWall(cnt+1)
                arr[i][j] = 0

makeWall(0)
print(result)