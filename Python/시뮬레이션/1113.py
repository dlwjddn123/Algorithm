from collections import deque

N, M = map(int, input().split())
pool = [list(map(int, input())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0

def go(x, y, n):
    global visited, result
    q = deque([x, y])
    check = True
    count = 1
    visited[y][x] = True
    while q:
        nx = q.popleft()
        ny = q.popleft()
        for i in range(4):
            if 0 <= dx[i] + nx <= M-1 and 0 <= dy[i] + ny <= N-1:
                if not visited[dy[i] + ny][dx[i] + nx] and pool[dy[i] + ny][dx[i] + nx] <= n :
                    visited[dy[i] + ny][dx[i] + nx] = True
                    q.append(dx[i] + nx)
                    q.append(dy[i] + ny)
                    count += 1
            else:
                check = False
                continue
    if check : 
        result += count 
    return

for i in range(1, 9):
    visited = [[False]*M for _ in range(N)]
    for j in range(N):
        for k in range(M):
            if pool[j][k] <= i and not visited[j][k]:
                go(k, j, i)

print(result)
