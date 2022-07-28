T = int(input())
result = []
for i in range(T):
    arr = []
    N = int(input())
    for i in range(N):
        n = list(map(int, input().split()))
        arr.append(n)

    arr.sort(key=lambda x : x[0])
    MIN = arr[0][1]
    count = 1
    for i in range(1,N):
        if arr[i][1] <= MIN:
            MIN = arr[i][1]
            count += 1 
    result.append(count)
    
for n in result:
    print(n)