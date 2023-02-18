import sys

input = sys.stdin.readline
N, M = map(int, input().split())
result = []
def dfs():
    if len(result) == M:
        print(*result)
        return
    for i in range(1, N+1):
        result.append(i)
        dfs()
        result.pop()
dfs()

