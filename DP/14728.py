N, T = map(int, input().split())
P = [[0, 0]]
dp = [[0]*(T+1) for _ in range(N+1)]
for _ in range(N):
    K, S = map(int, input().split())
    P.append([K, S])

for i in range(N+1):
    for j in range(T+1):
        Study_Time = P[i][0]
        Score = P[i][1]
        if Study_Time > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-Study_Time] + Score)

print(dp[N][T])


