N = int(input())
A = []
for _ in range(N):
    n = int(input())
    A.append(n)

A.sort()
result = 0
for i in range(N):
    result += abs(A[i] - (i + 1))

print(result)
