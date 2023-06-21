N = int(input())
T = []
P = []
dp = [0 for _ in range(N)]

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N):
    if i + T[i] -1 <= N-1:
        dp[i] += P[i]
        if i + T[i] < N:
            dp[i+T[i]] = max(dp[i], dp[i+T[i]])
    for j in range(i+T[i], N):
        if j + T[j] -1 <= N-1:
            if j + T[j] <= N:
                dp[j] = max(dp[i], dp[j])

print(max(dp))