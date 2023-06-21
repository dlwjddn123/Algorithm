N, K = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0 for _ in range(N+1)]
for i in range(1, N+1):
    sums[i] = nums[i-1] + sums[i-1]
MAX = -1000000000
for j in range(N+1-K):
    if sums[j+K] - sums[j] > MAX:
        MAX =  sums[j+K] - sums[j]
print(MAX)
