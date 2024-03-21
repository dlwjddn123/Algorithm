from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1 ,0, 0]

def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(bfs(maps, visited, i, j))

    answer.sort()
    
    if len(answer) == 0:
        answer.append(-1)
        
    return answer

def bfs(maps, visited, y, x):
    queue = deque()
    queue.append([x, y])
    visited[y][x] = True
    count = int(maps[y][x])
    N, M = len(maps), len(maps[0])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and maps[ny][nx] != 'X':
                count += int(maps[ny][nx])
                visited[ny][nx] = True
                queue.append([nx, ny])
    return count
    
    