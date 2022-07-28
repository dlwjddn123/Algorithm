import sys
input = sys.stdin.readline
N = int(input())
arr = []
plus = 0
zero = 0
minus = 0

for _ in range(N):
    n = list(map(int, input().split()))
    arr.append(n)

def cut(N, x, y):
    global plus
    global zero
    global minus
    if N == 0:
        return 
    success = False
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[y+i][x+j] == 1:
                count += 1
                if count == N*N:
                    plus += 1
                    success = True
            else:
                break
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[y+i][x+j] == 0:
                count += 1
                if count == N*N:
                    zero += 1
                    success = True
            else:
                break
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[y+i][x+j] == -1:
                count += 1
                if count == N*N:
                    minus += 1
                    success = True
            else:
                break   
    if not success:
        xx = [x, x, x, x+(N//3), x+(N//3), x+(N//3), x+(2*N//3), x+(2*N//3), x+(2*N//3)]
        yy = [y, y+(N//3), y+(2*N//3), y, y+(N//3), y+(2*N//3), y, y+(N//3), y+(2*N//3)] 
        for i in range(9):
            cut(N//3, xx[i], yy[i])

cut(N,0,0)
print(minus)
print(zero)
print(plus)

         

            
