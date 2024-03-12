N, M = int(input()), int(input())
broken = []
if M != 0:
    broken = list(map(int, input().split()))
number = [i for i in range(10)]
nums = []
result = [abs(N-100)]
for n in broken:
    number.remove(n)

def go(length, currentNums):
    if len(currentNums) == length:
        nums.append(int(currentNums))
        return 
    for n in number:
        currentNums += str(n)
        go(length, currentNums)
        currentNums = currentNums[:-1]

go(len(str(N)), "")
go(len(str(N)) + 1, "")
if len(str(N)) > 1:
    go(len(str(N)) - 1, "")

for num in nums:
    result.append(abs(N-num) + len(str(num)))

print(min(result))