from collections import deque


N, M = map(int, input().split())
MAP = [list(map(int, input())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[[False, 0] for _ in range(M)] for _ in range(N)]
q = deque()
q.append([0, 0, 1, 1])
result = []
visited[0][0][0] = True
while q:
    x, y, cost, chance = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= M-1 and 0 <= ny <= N-1:
            if visited[ny][nx][0] == False:
                if MAP[ny][nx] == 0:
                    visited[ny][nx][0] = True
                    if chance == 1:
                        visited[ny][nx][1] = 2
                    else:
                        visited[ny][nx][1] = 1

                    if (ny, nx) == (N-1, M-1):
                        result.append(cost+1)
                        continue     
                    q.append([nx, ny, cost+1, chance])
                else:
                    if chance == 1:
                        q.append([nx, ny, cost+1, chance-1])
            else:
                if visited[ny][nx][1] == 1 and chance == 1:
                    visited[ny][nx][1] = 2
                    q.append([nx, ny, cost+1, chance])
if (N+M) == 2:
    print(1)
elif len(result) == 0:
    print(-1)
else:
    print(min(result))

        



