from collections import deque
N, M = map(int, input().split())
figure = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for _ in range(N):
    temp = list(map(int, list(input())))
    figure.append(temp)

visited = [[False]* M for _ in range(N)]

def bfs(x):
    q = deque()
    q.append([x, 0])
    while q:
        x, y = q.popleft()
        visited[y][x] = True
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx <= M-1 and 0 <= ny <= N-1 and not visited[ny][nx]:
                if figure[ny][nx] == 0:
                    visited[ny][nx] = True
                    q.append([nx, ny])

for i in range(M):
    if figure[0][i] == 0:
        bfs(i)

if True in visited[-1]:
    print("YES")
else:
    print("NO")


