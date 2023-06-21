N, M, K = map(int, input().split())
fee = [0] + list(map(int, input().split()))
friends = [list(map(int, input().split())) for _ in range(M)]
parent = [i for i in range(N+1)]
def reunion(p, c):
    for i in range(1, N+1):
        if parent[i] == p:
            parent[i] = c

def union(x, y):
    a = find(x)
    b = find(y)
    for j in range(1, N+1):
        if parent[j] == y:
            parent[j] = b
    if fee[a] < fee[b]:
        reunion(parent[b], a)
        parent[b] = a
    elif fee[a] > fee[b]:
        reunion(parent[a], b)
        parent[a] = b
    else:
        if a < b:
            reunion(parent[b], a)
            parent[b] = a
        else:
            reunion(parent[a], b)
            parent[a] = b

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

for i in range(M):
    union(friends[i][0], friends[i][1])

already_count = []
total_fee = 0
flag = True

for j in range(1, N+1):
    if parent[j] not in already_count:
        already_count.append(parent[j])
        total_fee += fee[parent[j]]
        K -= fee[parent[j]]

if K >= 0:
    print(total_fee)
else:
    print("Oh no")