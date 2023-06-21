N, M = map(int, input().split())
know = list(map(int, input().split()))[1:]
party = [list(map(int, input().split()))[1:] for _ in range(M)]
parent = [i for i in range(N+1)]

def union(x, y):
    a = find(x)
    b = find(y)
    if a in know and b in know:
        return 
    elif a in know:
        parent[b] = a
    elif b in know:
        parent[a] = b
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

for i in range(len(party)):
    for j in range(len(party[i])-1):
        union(party[i][j], party[i][j+1])

result = 0

for i in range(len(party)):
    flag = True
    for j in range(len(party[i])):
        if find(party[i][j]) in know:
            flag = False
            break
    if flag:
        result += 1

print(result)

