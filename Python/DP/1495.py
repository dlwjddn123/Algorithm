n,s,m = map(int,input().split())
lst = list(map(int,input().split()))
dp = [[0] * (m+1) for i in range(n+1)]
dp[0][s] = True

for i in range(n):
    for j in range(m+1):
        if dp[i][j]:
            if j + lst[i] <= m:
                dp[i+1][j + lst[i]] = True
            if j - lst[i] >= 0:
                dp[i+1][j - lst[i]] = True
result = -1

for x in range(m+1):
    if dp[n][x]:
        result = x

print(result)