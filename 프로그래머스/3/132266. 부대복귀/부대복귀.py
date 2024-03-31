import heapq

def solution(n, roads, sources, destination):
    INF = 10 ** 8
    answer = []
    graph = [[] for _ in range(n+1)]
    distance = [INF for _ in range(n+1)]
    
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)
    
    hq = []
    heapq.heappush(hq, (0, destination))
    distance[destination] = 0
    
    while hq:
        dist, node = heapq.heappop(hq)
        
        if distance[node] < dist:
            continue
        
        for next_node in graph[node]:
            cost = distance[node] + 1
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(hq, [cost, next_node])
    
    for source in sources:
        if distance[source] == INF:
            answer.append(-1)
        else:
            answer.append(distance[source])
        
    return answer
    
    