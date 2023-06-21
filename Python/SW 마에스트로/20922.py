from collections import deque
N, K = map(int, input().split())
nums = list(map(int, input().split()))
hashNum = dict()
for i in range(200001):
    hashNum[i] = 0

start, end = 0, 1
temp = deque()
MAX = 0
temp.append(nums[start])
hashNum[nums[start]] += 1


while start < N and end < N:
    hashNum[nums[end]] += 1
    temp.append(nums[end])
    while hashNum[nums[end]] > K:
        idx = temp.popleft()
        hashNum[idx] -= 1
        start += 1
    if MAX < len(temp):
        MAX = len(temp)
    end += 1
print(MAX)

        
