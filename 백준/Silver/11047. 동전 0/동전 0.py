N, K = map(int, input().split())
coins = []
count = 0

for _ in range(N):
    coins.append(int(input()))

for i in range(1, N+1):
    if K >= coins[-i]:
        c = K // coins[-i]
        count += c
        K -= c * coins[-i]

print(count)