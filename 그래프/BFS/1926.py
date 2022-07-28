from collections import deque
N, M = map(int, input().split())
arr = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = []
count = 0
for _ in range(N):
    n = list(map(int, input().split()))
    arr.append(n)

def bfs(x, y):
    q = deque([x, y])
    count = 0
    while q:
        nx = q.popleft()
        ny = q.popleft()
        for i in range(4):
            if 0 <= nx + dx[i] <= M-1 and 0 <= ny + dy[i] <= N-1:
                if arr[ny+dy[i]][nx+dx[i]] == 1:
                    count += 1
                    q.append(nx+dx[i])
                    q.append(ny+dy[i])
                    arr[ny+dy[i]][nx+dx[i]] = 0
    result.append(count)

for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            bfs(j, i)
            count += 1
print(count)
if count:
    if max(result) == 0:
        print(1)
    else:
        print(max(result))
else:
    print(0)
    


 
