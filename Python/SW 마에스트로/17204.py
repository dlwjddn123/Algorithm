N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
count = 1
idx = 0
while True:
    if nums[idx] == K:
        break
    idx = nums[idx]
    count += 1
    if count == N:
        count = -1
        break
print(count)