N = int(input())
arr = []

for _ in range(N):
    n = int(input())
    arr.append(n)

arr.sort(reverse=True)
result = []
for i in range(N):
    result.append(arr[i]*(i+1))

print(max(result))
    