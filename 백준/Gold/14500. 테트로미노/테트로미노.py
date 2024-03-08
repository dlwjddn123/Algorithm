N, M = map(int,input().split())
arr = []
for _ in range(N):
    n = list(map(int, input().split()))
    arr.append(n)

x = [[0,1,2,3],[0,0,0,0],[0,1,0,1],[0,0,0,1],[0,1,2,0],[0,1,1,1],[0,1,2,2],[0,1,1,1],[0,0,1,2],[0,0,0,1],[0,1,2,2],[0,0,1,1],[0,1,1,2],[0,0,1,1],[0,1,1,2],[0,0,0,1],[0,1,1,2],[0,1,1,2],[0,1,1,1]]
y = [[0,0,0,0],[0,1,2,3],[0,0,1,1],[0,1,2,2],[0,0,0,1],[0,0,1,2],[1,1,1,0],[2,2,1,0],[0,1,1,1],[0,1,2,0],[0,0,0,1],[0,1,1,2],[1,1,0,0],[2,1,1,0],[0,0,1,1],[0,1,2,1],[1,1,0,1],[0,0,1,0],[1,0,1,2]]
MAX = []
def findMax(x, y):
    global N
    global M
    result = []
    i = 0
    count = 0
    while True:
        total = 0
        check = True
        for j in range(4):
            if x[j] + i >= M:
                count += 1
                i = -1
                check = False
            elif y[j] + count >= N:
                return max(result)
            else:
                total += arr[y[j]+count][x[j]+i]
        if check:
            result.append(total)
        else:
            pass
        i += 1

for i in range(len(x)):
    MAX.append(findMax(x[i],y[i]))

print(max(MAX))
    