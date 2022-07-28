N = int(input())
dp = [0,0]
for i in range(2,N+1):
    case = []
    if i % 3 == 0:
        case.append(dp[i//3])
    if i % 2 == 0:
        case.append(dp[i//2])
    case.append(dp[i-1])
    dp.append(min(case)+1)

print(dp[N])