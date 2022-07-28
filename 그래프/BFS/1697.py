from collections import deque

N, K = map(int, input().split())
MAX = 100000
dist = [0] * (MAX+1)

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            return
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx) 

bfs()
        