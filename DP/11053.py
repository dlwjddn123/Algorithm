N = int(input())
arr = list(map(int,input().split()))
length = 0
dp = []

for i in range(N):
    length = 1
    for j in range(i):
        if arr[i] > arr[j]:
            length = max(length, dp[j]+1)
    dp.append(length)

print(max(dp))



    