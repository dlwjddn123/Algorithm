N, M = map(int,input().split())
brands = []
result = [0 for _ in range(M)]
for _ in range(M):
    n = list(map(int, input().split()))
    brands.append(n)
for i in range(M):
    T = N
    while T >= 0 :
        if brands[i][1] * T <= brands[i][0]:
            result[i] += brands[i][1] * T
            break
        elif brands[i][0] >= brands[i][1] * 6 : 
            if T >= 6 :
                T -= 6
                result[i] += brands[i] 

print(result)
