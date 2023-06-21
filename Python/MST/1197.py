V, E = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(E)]
G.sort(key=lambda x : x[2])
parent = [i for i in range(V+1)]

def union(x, y):
    x, y = find(x), find(y)
    parent[x] = y

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

result = 0
for n in G:
    x, y, w = n[0], n[1] ,n[2]
    if find(x) != find(y):
        union(x, y)
        result += w
print(result)
