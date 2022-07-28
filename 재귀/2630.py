N = int(input())
arr = []
blue = 0
white = 0

for _ in range(N):
    n = list(map(int, input().split()))
    arr.append(n)

def cut(N, x, y):
    global blue
    global white
    if N == 0:
        return 
    success = False
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[y+i][x+j] == 1:
                count += 1
                if count == N*N:
                    blue += 1
                    success = True
            else:
                break
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[y+i][x+j] == 0:
                count += 1
                if count == N*N:
                    white += 1
                    success = True
            else:
                break
    
    if not success:
        xx = [x, x, x+(N//2), x+(N//2)]
        yy = [y, y+(N//2), y, y+(N//2)] 
        for i in range(4):
            cut(N//2, xx[i], yy[i])

cut(N,0,0)
print(white)
print(blue)

         

            
