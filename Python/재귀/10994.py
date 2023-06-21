N = int(input())
n = 4*N - 3
arr = [[" "for _ in range(n)]for _ in range(n)]

def star(N, x, y):
    if N == 1:
        arr[y][x] = "*"
        return
    n = 4*N - 3
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n:
                arr[y][x+j] = "*"
                arr[y+n-1][x+j] = "*"
            else:
                arr[y+i][x] = "*"
                arr[y+i][x+n-1] = "*"

    star(N-1,x+2,y+2)

star(N,0,0)
for n in arr:
    print("".join(n))