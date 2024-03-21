from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(maps):
    answer = 0
    leaver, run = 0, 0
    N, M = len(maps), len(maps[0])
    S, L, E = [], [], []
    
    for i in range(len(maps)):
        maps[i] = maps[i].strip()
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                S = [i, j]
            elif maps[i][j] == 'L':
                L = [i, j]
            elif maps[i][j] == 'E':
                E = [i, j]

    leaver += bfs(maps, S[0], S[1], 'L')
    
    if leaver != 0:
        run = bfs(maps, L[0], L[1], 'E')
    
    if leaver != 0 and run != 0:
        answer = leaver + run
    else:
        answer = -1
    return answer

def bfs(maps, y, x, target):
    queue = deque()
    queue.append([x, y, 0])
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    visited[y][x] = True
    N, M = len(maps), len(maps[0])
    
    while queue:
        x, y, count = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and maps[ny][nx] != 'X':       
                if maps[ny][nx] == target:
                    return count + 1
                visited[ny][nx] = True
                queue.append([nx, ny, count + 1])
                
    return 0
    