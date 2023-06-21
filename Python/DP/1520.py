N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1 for _ in range(M)]for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1
    if visited[y][x] != -1:
        return visited[y][x]

    visited[y][x] = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx <= M-1 and 0 <= ny <= N-1:
            if Map[ny][nx] < Map[y][x]:
                visited[y][x] += dfs(nx, ny)
    return visited[y][x]

print(dfs(0, 0))
    
        