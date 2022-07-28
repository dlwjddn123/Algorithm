N = int(input())
arr = []
for _ in range(N):
    n = int(input())
    arr.append(n)
if N < 3:
    print(sum(arr))
else:
    dp = []
    dp.append(arr[0])
    dp.append(arr[0]+arr[1])
    dp.append(max(arr[0]+arr[2], arr[1]+arr[2], arr[0]+arr[1]))
    for x in range(3, N):
        dp.append(max(dp[x-3]+arr[x-1]+arr[x], dp[x-2] + arr[x], dp[x-1]))
    print(dp[-1])


