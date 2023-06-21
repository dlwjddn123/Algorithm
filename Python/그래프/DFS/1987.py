import sys
input = sys.stdin.readline
R, C = map(int, input().split())
Map = []
for _ in range(R):
    Map.append(list(input()))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = 0
visited = set()
def dfs(count, x, y):
    global result
    result = max(result, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= C-1 and 0 <= ny <= R-1 and not Map[ny][nx] in visited:
            visited.add(Map[ny][nx])
            dfs(count+1, nx, ny)
            visited.remove(Map[y+dy[i]][x+dx[i]])
    

dfs(1, 0, 0)
print(result)

