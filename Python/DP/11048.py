N, M = map(int, input().split())
arr = []
case = []
for i in range(N):
    n = list(map(int, input().split()))
    arr.append(n)
    
for i in range(N):
    for j in range(M):
        if i == 0:
            if j == 0:
                continue
            arr[i][j] += arr[i][j-1]
        elif j == 0:
            arr[i][j] += arr[i-1][j]
        else:
            arr[i][j] += max(arr[i-1][j], arr[i-1][j-1], arr[i][j-1])

print(arr[N-1][M-1])