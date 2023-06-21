from collections import deque
N, M = map(int, input().split())
war = [list(input()) for _ in range(M)]
dx = [0, 0, -1 ,1]
dy = [-1, 1, 0, 0]
visited = [[False]*N for _ in range(M)]
def bfs(x, y, team):
    q = deque()
    q.append([x, y])
    count = 1
    visited[y][x] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[ny][nx] and war[ny][nx] == team:
                visited[ny][nx] = True
                q.append([nx, ny])
                count += 1
    return count
result = [0, 0]
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            if war[i][j] == "W":
                result[0] += bfs(j, i, "W") ** 2
            if war[i][j] == "B":
                result[1] += bfs(j, i, "B") ** 2

print(*result) 

                
 

