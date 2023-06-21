import heapq, sys

input = sys.stdin.readline
inf = int(1e8)

N = int(input())
M = int(input())
min_cost = [inf for _ in range(N+1)]
city = [[] for _ in range(N+1)]

for i in range(M):
    s, e, cost = map(int, input().split())
    city[s].append((e, cost))

start, end = map(int, input().split())

def dijkstra(start):
    pq = [(0, start)]
    min_cost[start] = 0
    while pq:
        total_cost, node = heapq.heappop(pq)
        if min_cost[node] < total_cost:
            continue
        for nxt_node, cost in city[node]:
            if min_cost[nxt_node] <= cost + total_cost:
                continue
            min_cost[nxt_node] = cost + total_cost
            heapq.heappush(pq, (cost + total_cost, nxt_node))

dijkstra(start)
print(min_cost[end])


