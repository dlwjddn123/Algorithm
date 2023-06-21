n, k = map(int, input().split())
arr = [0 for _ in range(k+1)]
arr[0] = 1

for _ in range(n):
    x = int(input())
    for i in range(1, k+1):
        if i - x >= 0:
            arr[i] += arr[i-x]

print(arr[-1])


