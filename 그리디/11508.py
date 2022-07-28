N = int(input())
C = [int(input()) for _ in range(N)]
C.sort(reverse=True)
result = 0
for i in range(N):
    if (i+1) % 3 == 0:
        continue
    result += C[i]

print(result)
