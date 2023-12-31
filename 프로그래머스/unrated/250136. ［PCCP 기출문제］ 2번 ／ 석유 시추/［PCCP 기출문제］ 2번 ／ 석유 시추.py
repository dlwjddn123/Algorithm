from collections import deque
            
def bfs(x, y, land, sectionNumber, visited):
    q = deque()
    q.append([x, y])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    amount = 1
    visited[y][x] = True
    land[y][x] = sectionNumber
    while q:
        tx, ty = q.popleft()
        for i in range(4):
            nx, ny = tx + dx[i], ty + dy[i]
            if 0 <= nx < len(land[0]) and 0 <= ny < len(land) and not visited[ny][nx] and land[ny][nx] == 1:
                land[ny][nx] = sectionNumber
                amount += 1
                visited[ny][nx] = True
                q.append([nx, ny])
    return amount

def solution(land):
    maxOilAmount = 0
    sections = [0, 0]
    sectionNumber = 2
    visited = [[False]* len(land[0]) for _ in range(len(land))]
    for i in range(len(land[0])):
        oilAmount = 0
        visitedSection = set()
        for j in range(len(land)):
            if not visited[j][i] and land[j][i] == 1:
                sections.append(bfs(i, j, land, sectionNumber, visited))
                sectionNumber += 1
            if land[j][i] not in visitedSection:
                visitedSection.add(land[j][i])
                oilAmount += sections[land[j][i]]
        if oilAmount > maxOilAmount:
            maxOilAmount = oilAmount
    
    return maxOilAmount