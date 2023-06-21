from collections import deque


N = int(input())
area = []
hst = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
Answer = 0
for _ in range(N):
    n = list(map(int, input().split()))
    m = max(n)
    if m > hst:
        hst = m
    area.append(n)

def bfs(h):
    global N, area, Answer
    visited = [[True]*(N) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] <= h:
                visited[i][j] = False
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                q = deque([j, i])
                chk = False
                while q:
                    chk = True
                    x = q.popleft()
                    y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                            if visited[ny][nx]:
                                visited[ny][nx] = False
                                q.append(nx)
                                q.append(ny)
                if chk:
                    result += 1
    if result > Answer :
        Answer = result

for i in range(hst+1):
    bfs(i)

print(Answer)

                         



