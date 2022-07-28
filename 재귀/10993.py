N = int(input())
h = 2**N - 1
w = 2**(N+1) - 3
arr = [[" "for _ in range(w)]for _ in range(h)]
def star(n, x, y):
    if n == 1:
        arr[y][x] = '*'
        return
    h = 2**n - 1
    w = 2**(n+1) - 3
    left = 0
    right = w-1
    if n % 2 == 0: 
        for i in range(h):
            for j in range(w):
                if i == 0:
                    arr[y][x+j] = "*"
                else:
                    arr[y+i][x+left+i] = "*"
                    arr[y+i][x+right-i] = "*"
        star(n-1,x+(h//2)+1,y+(h//2))

    else:
        if n == N:
            count = 0
            for i in range(h-1,-1,-1):
                for j in range(w):
                    if i == h-1:
                        arr[i][j] = "*"
                    else:
                        arr[i][left+count] = "*"
                        arr[i][right-count] = "*"
                count += 1
            star(n-1,h//2+1,h//2)

        else:
            for i in range(h):
                for j in range(w):
                    if i == 0:
                        arr[y][x+j] = "*"
                    else:
                        arr[y-i][x+left+i] = "*"
                        arr[y-i][x+right-i] = "*"
            star(n-1,x+(h//2)+1,y-(h//2))           

star(N, 0, 0)
for i in range(h):
    for j in range(w-1,-1,-1):
        if arr[i][j] == "*":
            break
        else:
            arr[i][j] = ''

for x in arr:
    print("".join(x))


