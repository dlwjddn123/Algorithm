N, L = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
result = 0

def ramp(y, x, h, isRow):
    if not isRow:
        for i in range(x, x+L):
            if 0 <= i < N and not rampPos[i] and Map[y][i] == h:
                rampPos[i] = True
                continue
            return False
        return True
    else:
        for i in range(y, y+L):
            if 0 <= i < N and not rampPos[i] and Map[i][x] == h:
                rampPos[i] = True
                continue
            return False
        return True

for i in range(N):
    rampPos = [False for _ in range(N)]
    for j in range(N-1):
        if abs(Map[i][j] - Map[i][j+1]) > 1:
            break 
        if Map[i][j] > Map[i][j+1] and Map[i][j] - Map[i][j+1] == 1:
            if not ramp(i, j+1, Map[i][j+1], False):
                break
        if Map[i][j] < Map[i][j+1] and Map[i][j+1] - Map[i][j] == 1:
            if not ramp(i, j-L+1, Map[i][j-L+1], False):
                break
        if j == N-2:
            result += 1

    rampPos = [False for _ in range(N)]

    for k in range(N-1):
        if abs(Map[k][i] - Map[k+1][i]) > 1:
            break

        if Map[k][i] > Map[k+1][i] and Map[k][i] - Map[k+1][i] == 1:
            if not ramp(k+1, i, Map[k+1][i], True):
                break
        if Map[k][i] < Map[k+1][i] and Map[k+1][i] - Map[k][i] == 1:
            if not ramp(k-L+1, i, Map[k-L+1][i], True):
                break
        if k == N-2:
            result += 1

print(result)
