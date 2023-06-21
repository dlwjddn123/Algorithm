N = int(input())
R = [1, 5, 10, 50]
nums = []
result = set()
def go(next):
    if len(nums) == N:
        result.add(sum(nums))
        return
    for i in range(next, 4):
        nums.append(R[i])
        go(i)
        nums.pop()
go(0)
print(len(result))