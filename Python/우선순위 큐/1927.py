import heapq

N = int(input())
hq = []
result = []
for _ in range(N):
    n = int(input())
    if n == 0:
        if len(hq) == 0:
            result.append(0)
        else:
            result.append(heapq.heappop(hq))
    else:
        heapq.heappush(hq, n)

for n in result:
    print(n)


