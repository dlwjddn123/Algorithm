N = int(input())
p = list(map(int, input().split()))
dp = [0] + p

for i in range(2, N+1):
    collections = []
    for j in range(1, i//2 + 1):
        collections.append([j, i-j])
    
    for n in collections:
        if dp[i] > dp[n[0]] + dp[n[1]]:
            dp[i] = dp[n[0]] + dp[n[1]]

print(dp[N])