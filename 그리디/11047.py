N, K = map(int, input().split())
A = []
Sum = K
count = 0
for _ in range(N):
    n = int(input())
    A.append(n)
idx = N-1
while Sum != 0:
    if Sum - A[idx] >= 0:
        count += 1
        Sum -= A[idx]
    else:
        idx -= 1

print(count) 

