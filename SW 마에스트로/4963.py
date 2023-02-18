from collections import deque

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
result = []

def bfs(x, y):
    global count
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < w and 0 <= ny < h and island[ny][nx] == 1:
                island[ny][nx] = 2
                q.append([nx, ny])
    count += 1

while True:
    w, h = map(int, input().split())
    island = []
    if w == h == 0:
        break
    for _ in range(h):
        island.append(list(map(int, input().split())))
    count = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                bfs(j, i)
    result.append(count)
for n in result:
    print(n)