from collections import deque


N = int(input())
G = []
for _ in range(N):
    G.append(list(map(int, input().split())))

visited = [[0]*N for _ in range(N)]
def bfs(x):
    print(q)
    q = deque([x])
    chk = [0]*N
    while q:
        n = q.popleft()
        for i in range(N):
            if chk[i] == 0 and G[n][i] == 1:
                chk[i] = 1
                visited[x][i] = 1
                q.append(i)
        
for i in range(N):
    bfs(i)

for n in visited:
    print(*n)



