import sys
input = sys.stdin.readline
N, M = map(int, input().split())
G = []
parent = [i for i in range(N+1)]
for _ in range(M+1):
    a, b, c = map(int, input().split())
    G.append([c,a,b])
G.sort()

def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]
W = 0
for i in range(M+1):
    w, x, y = G[i]
    if find(x) != find(y):
        union(x, y)
        if w == 0:
            W += 1

parent = [i for i in range(N+1)]
B = 0
for i in range(M, -1, -1):
    w, x, y = G[i]
    if find(x) != find(y):
        union(x, y)
        if w == 0:
            B += 1
print(W**2 - B**2)


