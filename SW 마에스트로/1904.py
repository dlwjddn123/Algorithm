N = int(input())
if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    dp = [2, 3]
    for i in range(N-2):
        temp = dp[1] 
        dp[1] = (dp[0] + dp[1]) % 15746
        dp[0] = temp

    print(dp[0])