from collections import deque

N, K = map(int, input().split())
road = [list(map(int, input())) for _ in range(2)]
visitedL = [False for _ in range(N)]
visitedR = [False for _ in range(N)]
move = [1, -1]
def bfs(direct, idx):
    q = deque()
    q.append([0, 0, 0])
    visitedL[0] = True
    while q:
        d, i, t = q.popleft()
        for j in range(3):
            next = i
            if j == 2:
                next += K
                if next >= N:
                    return 1
                if next <= t:
                    continue
                if 0 <= next and d == 0 and road[1][next] == 1 and not visitedR[next]:
                    visitedR[next] = True
                    q.append([1, next, t+1])
                
                elif 0 <= next and d == 1 and road[0][next] == 1 and not visitedL[next]:
                    visitedL[next] = True
                    q.append([0, next, t+1])
            else:
                next += move[j]
                if next >= N:
                    return 1
                if next <= t:
                    continue
                if 0 <= next and d == 0 and road[0][next] == 1 and not visitedL[next]:
                    visitedL[next] = True
                    q.append([0, next, t+1])
                
                elif 0 <= next and d == 1 and road[1][next] == 1 and not visitedR[next]:
                    visitedR[next] = True
                    q.append([1, next, t+1])
    return 0

print(bfs(0, 0))