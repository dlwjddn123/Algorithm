N = int(input())
l = []
result = [0 for _ in range(N)]
for _ in range(N):
    x, y = map(int, input().split())
    t = (x, y)
    l.append(t)

for i in range(N):
    count = 1
    for j in range(N):
        if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            count += 1
    result[i] = count

print(*result)
