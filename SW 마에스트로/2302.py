N = int(input())
M = int(input())
vip = list(int(input()) for _ in range(M))
people = [False for _ in range(N+1)]
for n in vip:
    people[n] = True
result = []
dp = [1 for _ in range(N+1)]

for i in range(2, N+1):
    if people[i]:
        result.append(dp[i-1])
        continue
    if people[i-1]:
        continue
    dp[i] = dp[i-1] + dp[i-2]
result.append(dp[N])
answer = result[0]

for i in range(1, len(result)):
    answer *= result[i]
    
print(answer)


