from collections import deque

N = int(input())
M = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    graph[i][i] = 1
plan = list(map(int, input().split()))
def bfs(row, target):
    q = deque()
    q.append(row)
    visited[row] = True
    while q:
        row = q.popleft()
        for i in range(N):
            if graph[row][i] == 1 and i == target:
                    return i
            if not visited[i]:
                if graph[row][i] == 1:
                    q.append(i)
                    visited[i] = True
    return -1
start = plan[0]-1
for i in range(M):
    if start == -1:
        break
    visited = [False for _ in range(N)]
    start = bfs(start, plan[i]-1)
if start != -1:
    print("YES")
else:
    print("NO")


