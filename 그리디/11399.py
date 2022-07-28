N = int(input())
P = list(map(int, input().split()))
P.sort()
result = 0
SUM = 0
for i in range(N):
    if i == 0:
        SUM += P[i]
        result = P[i]
        continue
    SUM += P[i]
    result += SUM

print(result)
