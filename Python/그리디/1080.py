N, M = map(int, input().split())
matrixA = [list(map(int, list(input()))) for _ in range(N)]
matrixB = [list(map(int, list(input()))) for _ in range(N)]
count = 0
def reverse3x3(y, x):
    for i in range(y, y+3):
        for j in range(x, x+3):
            matrixA[i][j] = 1 - matrixA[i][j]

for i in range(N-2):
    for j in range(M-2):
        if matrixA[i][j] != matrixB[i][j]:
            count += 1
            reverse3x3(i, j)
check = True

for i in range(N):
    if check:        
        for j in range(M):
            if matrixA[i][j] != matrixB[i][j]:
                check = False
                break
    else:
        break

if check:
    print(count)
else:
    print(-1)
