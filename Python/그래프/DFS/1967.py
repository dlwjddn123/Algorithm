import sys
input = sys.stdin.readline

N = int(input())
nodes = [[] for _ in range(N+1)]
result = []

for _ in range(N-1):
    n1, n2, w = map(int, input().split())
    nodes[n1].append([n2, w])
    nodes[n2].append([n1, w])
    
def dfs(c, p, w):
    for x in nodes[c]:
        if x[0] == p:
            result.append([w, c])
            continue 
        dfs(x[0], c, w + x[1])

if N == 1:
    print(0)
else:
    dfs(1, 0, 0)
    MAX = max(result)
    dfs(MAX[1], 0, 0)
    r = max(result)
    print(r[0])

