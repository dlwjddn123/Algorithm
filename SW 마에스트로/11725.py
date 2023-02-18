from collections import deque

N = int(input())
node = [[] for _ in range(N+1)]
parents = [0 for _ in range(N+1)]
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    node[n1].append(n2)
    node[n2].append(n1)

def bfs():
    q = deque()
    q.append(1)
    while q:
        t = q.popleft()
        for n in node[t]:
            node[n].remove(t)
            parents[n] = t
            q.append(n)
            
bfs()
for i in range(2, N+1):
    print(parents[i])