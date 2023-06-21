N = int(input())
coordinate = [list(map(int, input().split())) for _ in range(N)]
coordinate.sort()
current = coordinate[0]
result = 0
for i in range(1, N):
    if coordinate[i][0] > current[1]:
        result += current[1] - current[0]
        current = coordinate[i]
        continue
    if coordinate[i][1] > current[1]:
        current[1] = coordinate[i][1]
result += current[1] - current[0]
print(result)