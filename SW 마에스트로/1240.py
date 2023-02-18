import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[False]*(N+1) for _ in range(N+1)]

for _ in range(N-1):
    node1, node2, distance = map(int, input().split())
    graph[node1][node2] = distance
    graph[node2][node1] = distance

resultNode = [list(map(int, input().split())) for _ in range(M)]

result = []
chk = False

def dfs(x, y, dist):
    global chk
    if chk:
        return 
    visited[x] = True
    temp = 0
    for i in range(1, N+1):
        if graph[x][i] != False and not visited[i]:
            temp = dist + graph[x][i]
            visited[i] = True
            if i == y:
                result.append(temp)
                chk = True
                return  
            dfs(i, y, temp)
    
for i in range(M):
    visited = [False for _ in range(N+1)]
    chk = False
    dfs(resultNode[i][0], resultNode[i][1], 0)

for n in result:
    print(n)

