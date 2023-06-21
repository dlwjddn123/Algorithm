N = int(input())
SCV = list(map(int, input().split()))
dp = [[[0 for _ in range(61)]for _ in range(61)]for _ in range(61)]
while len(SCV) < 3:
    SCV.append(0)
def dfs(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return 0
    if dp[a][b][c] != 0:
        return dp[a][b][c]
    dp[a][b][c] = 1 + min(
        dfs(max(a-9, 0), max(b-3, 0), max(c-1, 0)), dfs(max(a-9, 0), max(b-1, 0), max(c-3, 0)),
        dfs(max(a-3, 0), max(b-9, 0), max(c-1, 0)), dfs(max(a-3, 0), max(b-1, 0), max(c-9, 0)),
        dfs(max(a-1, 0), max(b-9, 0), max(c-3, 0)), dfs(max(a-1, 0), max(b-3, 0), max(c-9, 0))
    )
    return dp[a][b][c]

print(dfs(SCV[0],SCV[1],SCV[2]))