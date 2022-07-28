N = int(input())
A = list(map(int, input().split()))
dp = [1 for _ in range(N)]
for i in range(N):
    temp = []
    for j in range(i):
        if  A[j] > A[i]:
            temp.append(dp[j])
    if len(temp) != 0:
        dp[i] += max(temp)

print(max(dp))
