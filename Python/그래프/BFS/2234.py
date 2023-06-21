from collections import deque

N, M = map(int, input().split())

arr = []
temp = [[0]*N for _ in range(M)]
for _ in range(M):
    n = list(map(int, input().split()))
    arr.append(n)

Ans1 = 0
Ans2 = []
Ans3 = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
West = [0, 2, 4, 6, 8, 10, 12, 14]
South = [0, 1, 2, 3, 4, 5, 6, 7]
East = [0, 1, 2, 3, 8, 9, 10, 11]
North = [0, 1, 4, 5, 8, 9, 12, 13]
direct = [North, South, West, East]
c = 1
def bfs(x, y):
    global c
    q = deque([x, y])
    visited = [[False]*N for _ in range(M)]
    count = 1
    while q:
        nx = q.popleft()
        ny = q.popleft()
        temp[ny][nx] = c
        visited[ny][nx] = True
        for i in range(4):
            if 0 <= dx[i] + nx <= N-1 and 0 <= dy[i] + ny <= M-1:
                if arr[ny][nx] in direct[i]:
                    if not visited[ny + dy[i]][nx + dx[i]]:
                        temp[ny+ dy[i]][nx+ dx[i]] = c
                        q.append(nx + dx[i])
                        q.append(ny + dy[i])
                        visited[ny+dy[i]][nx+dx[i]] = True

for i in range(M):
    for j in range(N):
        if temp[i][j] == 0:
            bfs(j, i)
            c += 1
case = [set()for _ in range(c-1)]

Ans2 = [0 for _ in range(c-1)]
for i in range(M):
    for j in range(N):
        Ans2[temp[i][j]-1] += 1
        if i + 1 <= M-1:
            case[temp[i][j] - 1].add(temp[i+1][j])
        if j + 1 <= N-1:
            case[temp[i][j] - 1].add(temp[i][j+1])
MAX = set()
t = 1
for k in case:
    k = list(k)
    if t in k:
        k.remove(t)
    for i in k:
        MAX.add(Ans2[t-1]+Ans2[i-1])
    t += 1


print(c-1)
print(max(Ans2))
if len(MAX) == 0:
    print(1)
else:
    print(max(MAX))

