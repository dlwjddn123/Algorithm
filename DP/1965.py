N = int(input())

boxes =list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if boxes[i] > boxes[j] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))