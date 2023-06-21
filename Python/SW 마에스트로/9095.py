T = int(input())
n = [int(input()) for _ in range(T)]
dp = [0 for _ in range(11)]
dp[0] = 1
dp[1] = 2
dp[2] = 4
for i in range(3, max(n)):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for d in n:
    print(dp[d-1])



