from collections import deque


N, M = map(int, input().split())
r, c, d = map(int, input().split())
Map = [[] for _ in range(N)]
answer = 1
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

for i in range(N):
    n = list(map(int, input().split()))
    Map[i] = n
Map[r][c] = 2
def bfs():
    global d, answer
    visited = [[False]*M for _ in range(N)]
    if d == 1:
        d = 3
    elif d == 3:
        d = 1
    q = deque([r, c])
    while q:
        check = False
        dr = q.popleft()
        dc = q.popleft()
        for i in range(4):
            d += 1
            d = d % 4
            if Map[dr+dy[d]][dc+dx[d]] == 0:
                q.append(dr+dy[d])
                q.append(dc+dx[d])
                Map[dr+dy[d]][dc+dx[d]] = 2
                answer += 1
                check = True
                visited[dr+dy[d]][dc+dx[d]] = True
                break

        if not check:
            if Map[dr+dy[(d+2)%4]][dc+dx[(d+2)%4]] == 1:
                break
            else:
                q.append(dr+dy[(d+2)%4])
                q.append(dc+dx[(d+2)%4])
bfs()
print(answer)




