import sys
input = sys.stdin.readline

N = int(input())
arr = []
count = 0
for _ in range(N):
    n = list(map(int, input().split()))
    arr.append(n)


def pipe(x, y, direction): # 방향 가로는 0, 대각1, 세로 2
    global count
    if direction == 0: # 가로
        if x+1 < N :
            if arr[y][x+1] == 2:
                count += 1
                return
            elif arr[y][x+1] == 0:
                pipe(x+1, y, 0)
            else:
                return
        if x+1 < N and y+1 < N:
            if arr[y+1][x+1] == 2 and arr[y][x+1] == 0 and arr[y+1][x] == 0:
                count += 1
                return
            elif arr[y+1][x] == 0 and arr[y+1][x+1] == 0 and arr[y][x+1] == 0:
                pipe(x+1, y+1, 2)
            else:
                return
        else:
            return 

    elif direction == 1: # 세로
        if y+1 < N:
            if arr[y+1][x] == 2:
                count += 1
                return
            elif arr[y+1][x] == 0:
                pipe(x, y+1, 1)
            else:
                return
        if x+1 < N and y+1 < N:
            if arr[y+1][x+1] == 2 and arr[y][x+1] == 0 and arr[y+1][x] == 0:
                count += 1
                return
            elif arr[y+1][x] == 0 and arr[y+1][x+1] == 0 and arr[y][x+1] == 0:
                pipe(x+1, y+1, 2)
            else:
                return     
        else:
            return     

    elif direction == 2: # 대각
        if x+1 < N:
            if arr[y][x+1] == 2:
                count += 1
                return
            elif arr[y][x+1] == 0:
                pipe(x+1, y, 0)
            else:
                pass
        if y+1 < N:
            if arr[y+1][x] == 2:
                count += 1
                return
            elif arr[y+1][x] == 0:
                pipe(x, y+1, 1)
            else:
                return
        if x+1 < N and y+1 < N:
            if arr[y+1][x+1] == 2 and arr[y][x+1] == 0 and arr[y+1][x] == 0:
                count += 1
                return
            elif arr[y+1][x] == 0 and arr[y+1][x+1] == 0 and arr[y][x+1] == 0:
                pipe(x+1, y+1, 2)
            else:
                return     
        else:
            return
if arr[N-1][N-1] == 1:
    print(0)
else:
    arr[N-1][N-1] = 2
    pipe(1,0,0)
    print(count)

