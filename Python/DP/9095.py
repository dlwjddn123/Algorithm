T = int(input())
arr = []
result = [1, 2, 4]
for _ in range(T):
    n = int(input())
    arr.append(n)

Max = max(arr)

for i in range(3, Max):
    n = result[i-1] + result[i-2] + result[i-3]
    result.append(n)

for j in arr:
    print(result[j-1])


