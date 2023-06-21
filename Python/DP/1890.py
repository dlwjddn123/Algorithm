N = int(input())
arr = []
dp = [[-1]*N for _ in range(N)]
for _ in range(N):
    n = list(map(int, input().split()))
    arr.append(n)

def go(x, y):
    global dp
    if x == N-1 and y == N-1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0
    if x + arr[y][x] < N:
        dp[y][x] += go(x + arr[y][x], y)
    if y + arr[y][x] < N:
        dp[y][x] += go(x, y + arr[y][x])

    return dp[y][x]

print(go(0, 0))





        
