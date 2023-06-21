from itertools import combinations


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([j, i])
        elif city[i][j] == 2:
            chicken.append([j, i])
l = []
for n in home:
    for m in chicken:
        dist = abs(n[0] - m[0]) + abs(n[1] - m[1])
        city[m[1]][m[0]] += dist

result = 10000
for i in combinations(chicken, M):
    tmp = 0
    for j in home:
        minVal = 10000
        for k in i:
            distance = abs(k[0] - j[0]) + abs(k[1] - j[1])
            minVal = min(minVal, distance)
        tmp += minVal
    result = min(result, tmp)
print(result)