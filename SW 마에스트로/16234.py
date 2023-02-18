from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int ,input().split())
country = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
chk = False
def bfs(x, y):
    q = deque()
    q.append([x, y])
    moveCountry = [[x, y]]
    visited[y][x] = True
    total = country[y][x]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and L <= abs(country[y][x]-country[ny][nx]) <= R :
                visited[ny][nx] = True
                q.append([nx, ny])
                moveCountry.append([nx, ny])
                total += country[ny][nx]
    dayChange.append([moveCountry, total])
answer = 0
while True:
    chk = False
    dayChange = []
    visited = [[False] * (N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nj, ni = j + dx[k], i + dy[k]
                if 0 <= nj < N and 0 <= ni < N and not visited[ni][nj] and L <= abs(country[i][j]-country[ni][nj]) <= R:
                    bfs(nj, ni)
                    chk = True
    for c, t in dayChange:
        for x, y in c:
            country[y][x] = t // len(c)

    if not chk:
        break
    answer += 1

print(answer)


