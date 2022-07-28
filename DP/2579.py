import sys
input = sys.stdin.readline

N = int(input())
arr = [0]
result = []
for _ in range(N):
    n = int(input())
    arr.append(n)
    
g = [0, 0]
h = [0, arr[1]]
for x in range(2, N+1):
    g.append(h[x-1]+arr[x])
    h.append(max(g[x-2], h[x-2])+arr[x])
print(max(g[N], h[N]))
