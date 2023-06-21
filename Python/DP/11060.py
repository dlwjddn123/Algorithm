N = int(input())
arr = list(map(int,input().split()))
idx = 0
count = 0
while True:
    n = arr[idx]
    if n == 0:
        if idx == 0 and N == 1:
            count = 0
            break
        count = -1
        break

    Max = 0
    MaxIndex = idx
    temp = 0
    for i in range(1,n+1):
        MaxIndex += 1
        if arr[idx+i] + MaxIndex >= Max:
            Max = arr[idx+i] + MaxIndex
            temp = idx + i
    idx = temp
    count += 1
    if N == 2:
        break
    if idx + arr[idx] >= N-1:
        count += 1
        break

print(count)






