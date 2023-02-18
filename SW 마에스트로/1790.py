N, K = map(int, input().split())
nums = [1, 9]
for i in range(2, 9):
    nums.append(nums[i-1] + i * 10 **(i-1) * 9 - 1)

print(nums)
