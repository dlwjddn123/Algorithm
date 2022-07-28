N = int(input())
parents = list(map(int, input().split()))
M = int(input())
tree = {}

def dfs(n):
    global parents
    parents[n] = -2
    for i in range(len(parents)):
        if n == parents[i]:
            dfs(i)

dfs(M)
count = 0
for i in range(N):
    if parents[i] != -2 and i not in parents:
        count += 1

print(count)