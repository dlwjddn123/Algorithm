N = int(input())
Map = [list(map(int,input().split())) for _ in range(N)]
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for i in range(N):
    if Map[0][i] == 1:
        break
    else:
        dp[0][i][0] = 1

for i in range(1, N):
    for j in range(2, N):
        if Map[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
        if Map[i][j-1] == 0 and Map[i-1][j] == 0 and Map[i][j] == 0:
            dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(sum(dp[N-1][N-1]))




