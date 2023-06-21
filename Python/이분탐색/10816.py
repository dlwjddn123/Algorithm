N = int(input())
arr1 = list(map(int, input().split()))
D = dict()
for n in arr1:
    if n in D:
        D[n] += 1
    else:
        D[n] = 1

M = int(input())
arr2 = list(map(int, input().split()))
result = []
for i in range(M):
    if arr2[i] in D:
        result.append(D[arr2[i]])
    else:
        result.append(0)

print(*result)



