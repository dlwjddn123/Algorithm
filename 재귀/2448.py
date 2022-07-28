N = int(input())
arr = [[" "for _ in range(2*N)]for _ in range(N)]

def star(N, x, y):
    xx = [x, x+(N//2), x+N]
    yy = [y, y-(N//2), y]

    if N == 3:
        for i in range(3):
            for j in range(5):
                if i == 0:
                    arr[y-i][x+j] = "*"
                elif i == 1:
                    if j % 2 == 1:
                        arr[y-i][x+j] = "*"
                else:
                    if j == 2:
                        arr[y-i][x+j] = "*"
        return 
    for i in range(3):
        star(N//2, xx[i], yy[i])
star(N, 0, N-1)
for n in arr:
    print("".join(n))
