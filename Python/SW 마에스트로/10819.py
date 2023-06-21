N = int(input())
nums = list(map(int, input().split()))
result = []
pre = []
def go():
    if len(pre) == N:
        cal(pre)
        return
    for i in range(len(nums)):
        pre.append(nums[i])
        t = nums.pop(i)
        go()
        pre.pop()
        nums.insert(i, t)
        
def cal(arr):
    Sum = 0
    for i in range(1, len(arr)):
        Sum += abs(arr[i-1] - arr[i])
    result.append(Sum)

go()
print(max(result))