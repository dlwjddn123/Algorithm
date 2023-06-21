N = int(input())
candy = list(list(input()) for _ in range(N))
result = []
def checkX(x):
    start = candy[0][x]
    MAX = 0
    count = 1
    for i in range(1, N):
        if candy[i][x] == start:
            count += 1
            continue
        start = candy[i][x]
        if MAX < count:
            MAX = count
        count = 1
    if count > MAX:
        result.append(count)
    else:
        result.append(MAX)

def checkY(y):
    start = candy[y][0]
    MAX = 0
    count = 1
    for i in range(1, N):
        if candy[y][i] == start:
            count += 1
            continue
        start = candy[y][i]
        if MAX < count:
            MAX = count
        count = 1
    if count > MAX:
        result.append(count)
    else:
        result.append(MAX)
for i in range(N):
    for j in range(N):
        if j < N-1 and candy[i][j] != candy[i][j+1]:
            temp = candy[i][j]
            candy[i][j] = candy[i][j+1]
            candy[i][j+1] = temp
            checkX(j)
            checkX(j+1)
            checkY(i)
            temp = candy[i][j]
            candy[i][j] = candy[i][j+1]
            candy[i][j+1] = temp
        if i < N-1 and candy[i][j] != candy[i+1][j]:
            temp = candy[i][j]
            candy[i][j] = candy[i+1][j]
            candy[i+1][j] = temp
            checkY(i)
            checkY(i+1)
            checkX(j)
            temp = candy[i][j]
            candy[i][j] = candy[i+1][j]
            candy[i+1][j] = temp
            
for i in range(N):
    checkX(i)
    checkY(i)

print(max(result))