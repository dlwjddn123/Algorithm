import sys
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
parent = [x for x in range(N+1)]
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x,  y = find(x), find(y)
    parent[x] = y

for n in graph:
    f, start, end = n[0], n[1], n[2]
    if f == 0:
        union(start, end)
    else:
        if find(start) == find(end):
            print("YES")
        else:
            print("NO")
    