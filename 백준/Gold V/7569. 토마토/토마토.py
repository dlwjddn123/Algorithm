from collections import deque


M, N, H = map(int, input().split())
boxes = []
for i in range(H):
    n = [list(map(int, input().split())) for _ in range(N)]
    boxes.append(n)

days = 0
dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
visited = [[[False]*M for _ in range(N)] for _ in range(H)]
def bfs(s):
    global days, visited
    q1 = deque(s)
    while q1:
        q2 = deque(q1)
        q1.clear()
        chk = False
        while q2:
            nx = q2.popleft()
            ny = q2.popleft()
            nz = q2.popleft()
            for i in range(6):
                if 0 <= nx + dx[i] <= M-1 and 0 <= ny + dy[i] <= N-1 and 0 <= nz + dz[i] <= H-1:
                    if boxes[nz + dz[i]][ny + dy[i]][nx + dx[i]] == 0 and not visited[nz + dz[i]][ny + dy[i]][nx + dx[i]]:
                        visited[nz + dz[i]][ny + dy[i]][nx + dx[i]] = True
                        boxes[nz + dz[i]][ny + dy[i]][nx + dx[i]] = 1
                        chk = True
                        q1.append(nx + dx[i])
                        q1.append(ny + dy[i])
                        q1.append(nz + dz[i])
        if chk :
            days += 1
start = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 1:
                start.append(k)
                start.append(j)
                start.append(i)

bfs(start)
chk = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 0:
                chk = True
                break
if chk:
    print(-1)
else:   
    print(days)         


        

