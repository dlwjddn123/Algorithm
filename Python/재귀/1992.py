N = int(input())
arr = []
result = []
for _ in range(N):
    n = list(map(int, input()))
    arr.append(n)

def compression(N, x, y):
    count = 0
    success = False
    if N <= 0 :
        return
    for i in range(N):
        for j in range(N):
            if arr[y+i][x+j] == 1:
                count += 1
                if count == N*N:
                    result.append("1")
                    success = True
            else:
                break
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[y+i][x+j] == 0:
                count += 1
                if count == N*N:
                    success = True
                    result.append("0")
            else:
                break
    if not success:
        xx = [x, x+(N//2),x, x+(N//2)]
        yy = [y, y, y+(N//2), y+(N//2)]
        result.append("(")
        idx = 0
        for _ in range(2):
            for _ in range(2):
                compression(N//2, xx[idx], yy[idx])
                idx += 1
        result.append(")")

compression(N,0,0)
print("".join(result))
