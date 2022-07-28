T = int(input())
dp = [0, 1, 1, 1]
N = list(int(input()) for _ in range(T))
C = N[::]
M = max(N)
if M >= 4:
    for i in range(4, M+1):
        dp.append(dp[i-2] + dp[i-3])
for i in C:
    print(dp[i])





