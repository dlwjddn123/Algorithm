N = int(input())
student = [[0]*4 for _ in range(N*N+1)]
MAP = [[0]*N for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
order = []
for _ in range(N*N):
    n = list(map(int, input().split()))
    student[n[0]] = n[1:]
    order.append(n[0])

def solve1(n):
    MAX = 0
    coordinate = []
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 0 :
                count = 0 
                for k in range(4):
                    if 0 <= dx[k] + j <= N-1 and 0 <= dy[k] + i <= N-1:
                        if MAP[dy[k] + i][dx[k] + j] in student[n]:
                            count += 1
                if count > MAX:
                    MAX = count
                    coordinate = [[j, i]]
                elif count == MAX:
                    coordinate.append([j, i])
                else:
                    continue
    return coordinate            
        
def solve2(cd):
    MAX = 0
    coordinate = []
    for n in cd:
        count = 0
        for k in range(4):
            if 0 <= dx[k] + n[0] <= N-1 and 0 <= dy[k] + n[1] <= N-1:
                if MAP[dy[k] + n[1]][dx[k] + n[0]] == 0:
                    count += 1
        if count > MAX:
            MAX = count
            coordinate = [n]
        elif count == MAX:
            coordinate.append(n)
        else:
            continue
    return coordinate

def solve3(n, cd):
    cd.sort(key=lambda x:(x[1],x[0]))
    MAP[cd[0][1]][cd[0][0]] = n
                
for n in order:
    result1 = solve1(n)
    result2 = solve2(result1)
    solve3(n,result2)

total = 0
for i in range(N):
    for j in range(N):
        count = 0 
        for k in range(4):
            if 0 <= dx[k] + j <= N-1 and 0 <= dy[k] + i <= N-1:
                if MAP[dy[k] + i][dx[k] + j] in student[MAP[i][j]]:
                    count += 1
        if count == 0:
            continue
        else:
            total += 10**(count-1)

print(total)
