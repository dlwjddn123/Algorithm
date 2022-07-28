from collections import deque
import itertools


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

virus = []
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 2:
            virus.append([i, j])

comb = list(itertools.combinations(virus, M))
result = []        
def bfs(arr):
    visited = [[False]*N for _ in range(N)]
    COPY_MAP = []
    for i in range(N):
        COPY_MAP.append(MAP[i][::])
    for n in arr:
        COPY_MAP[n[0]][n[1]] = "S"
        visited[n[0]][n[1]] = True
    for i in range(N):
        for j in range(N):
            if COPY_MAP[i][j] == 1:
                COPY_MAP[i][j] = '-'
            elif COPY_MAP[i][j] == 2:
                COPY_MAP[i][j] = "*"                

    count = 1
    q = deque()
    q.append(arr)
    while q:
        temp = q.popleft()
        q2 = deque()
        for n in temp:
            q2.append(n)
        temp = []
        while q2:
            y, x = q2.popleft()
            visited[y][x] = True
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx <= N-1 and 0 <= ny <= N-1 and not visited[ny][nx]:
                    if COPY_MAP[ny][nx] != '-' and COPY_MAP[ny][nx] != "S":
                        visited[ny][nx] = True
                        temp.append([ny, nx])
                        if COPY_MAP[ny][nx] == "*":
                            continue
                        COPY_MAP[ny][nx] = count
        count += 1
        if len(temp) == 0:
            break
        else:
            q.append(temp)
    MAX = 0
    chk = False
    for i in range(N):
        if chk:
            break
        for j in range(N):
            if COPY_MAP[i][j] == "-" or COPY_MAP[i][j] == "*" or COPY_MAP[i][j] == "S":
                continue
            if COPY_MAP[i][j] == 0:
                MAX = -1
                chk = True
                break
            if COPY_MAP[i][j] > MAX:
                MAX = COPY_MAP[i][j]
    if not chk:
        result.append(MAX)
    
        
    

for n in comb:
    bfs(n)
if len(result) == 0:
    print(-1)
else:
    print(min(result))




