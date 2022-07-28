from collections import deque


N = int(input())
g = [[] for _ in range(N+1)]

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    g[n1].append(n2)
    g[n2].append(n1)

p = list(map(int, input().split()))

count = 1
def bfs(x):
    global count
    q = deque()
    q.append(x)
    while q:
        n = q.popleft()
        while True:
            if p[count] in g[n]:
                q.append(p[count])
                count += 1
                if count == N:
                    return 1
            else:
                break
    return 0
if p[0] != 1:
    print(0)
else:
    print(bfs(1))

            




