N = int(input())
dp = [0 for _ in range(N+1)]
dp[0] = 0
dp[1] = 0

for i in range(2, N+1):
    if i % 3 == 0:
        if i % 2 == 0:
            dp[i] = min([dp[i//3], dp[i//2], dp[i-1]]) + 1
            continue
        dp[i] = min(dp[i//3], dp[i-1]) + 1
        continue
    if i % 2 == 0:
        dp[i] = min(dp[i//2], dp[i-1]) + 1 
        continue
    dp[i] = dp[i-1] + 1

print(dp)



