from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(place, x, y):
    queue = deque()
    queue.append([x, y, 0])
    visited = [[False] * 5 for _ in range(5)]
    visited[y][x] = True
    
    while queue:
        x, y, dist = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[ny][nx]:
                if place[ny][nx] == 'P':
                    return False
                visited[ny][nx] = True
                if dist == 0 and place[ny][nx] == 'O':
                    queue.append([nx, ny, dist + 1])
    return True

def solution(places):
    answer = []
    check = True
    for place in places:
        for j in range(5):
            check = True
            for k in range(5):
                if place[j][k] == 'P':
                    check = bfs(place, k, j)
                    if not check:
                        break
            if not check:
                answer.append(0)
                break
        if check:
            answer.append(1)
    
    return answer