from collections import deque
T = int(input())
result = []
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[0]*(N+1) for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1
    
    q = deque()
    q.append(1)
    visited[1] = True
    total = 0
    while q:
        current = q.popleft()
        for i in range(1, N+1):
            if graph[current][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)
                total += 1
    result.append(total)
for n in result:
    print(n)


