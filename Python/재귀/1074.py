import sys
input = sys.stdin.readline

N, r, c= map(int, input().split())
N = 2**N
arr = []
count = -1
quadrant = 0
def Z(N, x, y):
    global count
    global c
    global r
    global quadrant
    if N <= 0:
        return
    elif N == 1:
        for i in range(2):
            for _ in range(2):
                count += 1
                arr.append(count)
    xx = [x, x+N, x, x+N]
    yy = [y, y, y+N, y+N]

    if r < y+N and c < x+N:
        if N == 1:
            quadrant = 0
        Z(N//2, xx[0], yy[0])

    elif r < y+N and c >= x+N:
        if N == 1:
            quadrant = 1
        count += N*N
        Z(N//2, xx[1], yy[1])

    elif r >= y+N and c < x+N:
        if N == 1:
            quadrant = 2
        count += 2*N*N
        Z(N//2, xx[2], yy[2])
        
    elif r >= y+N and c >= x+N:
        if N == 1:
            quadrant = 3
        count += 3*N*N
        Z(N//2, xx[3], yy[3])
    else:
        print("pass")

Z(N//2, 0, 0)
print(arr[quadrant])