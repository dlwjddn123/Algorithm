T = int(input())
result = []
for _ in range(T):
    arr = []
    cols = int(input())
    for _ in range(2):
        n = list(map(int,input().split()))
        arr.append(n)
    
    for i in range(1, cols):
        if i == 1:
            arr[0][i] += arr[1][i-1]
            arr[1][i] += arr[0][i-1]
        else:
            arr[0][i] += max(arr[1][i-1], arr[1][i-2])
            arr[1][i] += max(arr[0][i-1], arr[0][i-2])
    result.append(max(arr[0][cols-1], arr[1][cols-1]))

for n in result:
    print(n)