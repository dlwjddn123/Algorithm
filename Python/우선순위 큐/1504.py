import heapq
import sys

input = sys.stdin.readline
inf = int(1e8)

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())
min_dist = [inf for _ in range(N+1)]

def dijkstra(start):
    global min_dist
    min_dist = [inf for _ in range(N+1)]
    min_dist[start] = 0
    pq = [(start, 0)]
    while pq:
        node, weight = heapq.heappop(pq)
        if min_dist[node] < weight:
            continue
        for nxt_node, nxt_weight in graph[node]:
            if min_dist[nxt_node] <= weight + nxt_weight:
                continue
            min_dist[nxt_node] = weight + nxt_weight
            heapq.heappush(pq, (nxt_node, weight + nxt_weight))

dijkstra(1)
r1, r2 = min_dist[v1], min_dist[v1]
r3, r4 = min_dist[v2], min_dist[v2]
dijkstra(v1)
r1 += min_dist[v2] * 2 + min_dist[N]
r2 += min_dist[v2]
r4 += min_dist[N]
dijkstra(v2)
r2 += min_dist[N]
r3 += min_dist[v1] * 2 + min_dist[N]
r4 += min_dist[v1]

result = min(r1, r2, r3, r4)
if result >= inf:
    print(-1)
else:
    print(result)