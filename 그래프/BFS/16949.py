from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
MAP = [list(map(int, input().rstrip()))for _ in range(N)]
result = []
for i in range(N):
    result.append(MAP[i][::])

bundle = []
for i in range(N):
    bundle.append(MAP[i][::])

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
B = 2
visited = [[False]*M for _ in range(N)]
def bfs(y, x):
    global MAP, visited, B, bundle
    q = deque()
    q.append([x, y])
    count = 0
    chk = False
    idx = []
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if 0 <= nx <= M-1 and 0 <= ny <= N-1:
                if MAP[ny][nx] == 0 and not visited[ny][nx]:
                    chk = True
                    count += 1
                    visited[ny][nx] = True
                    q.append([nx, ny])
                    idx.append([nx, ny])
    if chk:
        for n in idx:
            MAP[n[1]][n[0]] = count
            bundle[n[1]][n[0]] = B
    else:
        MAP[y][x] = 1
        bundle[y][x] = B
    B += 1


for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0:
            bfs(i, j)

visited2 = [[False]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if result[i][j] == 1:
            t = 0
            visited2[i][j] = True
            temp = []
            for k in range(4):
                nx = dx[k] + j
                ny = dy[k] + i
                if 0 <= nx <= M-1 and 0 <= ny <= N-1:
                    if result[ny][nx] == 0 and not visited2[ny][nx]:
                        if bundle[ny][nx] not in temp:
                            temp.append(bundle[ny][nx])
                            t += MAP[ny][nx]
            result[i][j] = (t+1) % 10

for n in result:
    print(''.join(map(str, n)))

