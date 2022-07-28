N = int(input())
M = int(input())
graph = [list(map(int, input().split())) for _ in range(M)]
parent = [x for x in range(N+1)]
result = 0

graph.sort(key=lambda x : x[2])

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    parent[x] = y

for n in graph:
    start, end, weights = n[0], n[1], n[2]
    if find(start) != find(end):
        result += weights
        union(start, end)

print(result)

