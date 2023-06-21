i = 1
result = []
while True:
    k = int(input())
    if k == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(k)]
    graph[0][0], graph[0][2] = graph[0][1], graph[0][1] 
    for j in range(1, k):
        for x in range(3):
            if x == 0:
                graph[j][x] += min(graph[j-1][0], graph[j-1][1])
            elif x == 1:
                graph[j][x] += min(graph[j-1])
            elif x == 2:
                graph[j][x] += min(graph[j-1][1], graph[j-1][2])
    result.append([i, graph[k-1][1]])
    i += 1

for idx in range(len(result)):
    print(f"{result[idx][0]}. {result[idx][1]}")
