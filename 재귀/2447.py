N = int(input())
arr = [["*" for _ in range(N)]for _ in range(N)]

def clear(N, x, y):
    if N / 3 <= 0:
        return
    print(x,y)
    for i in range(3):
        for j in range(3):
            clear(N//3, x+(N//3)*j,y+(N//3)*i)
    
    for i in range(N//3, N//3 * 2):
        for j in range(N//3, N//3 * 2):
            arr[y+i][x+j] = " "
  

clear(N,0,0)

for i in arr:
    print(i)

   