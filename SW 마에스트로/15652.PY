N, M = map(int, input().split())
result = []
def dfs(startIdx):
    if len(result) == M:
        print(*result)
        return 
    
    for i in range(startIdx, N+1):
        result.append(i)
        dfs(i)
        result.pop()

dfs(1)
    