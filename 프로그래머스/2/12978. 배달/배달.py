def solution(N, road, K):
    answer = 0
    INF = 10**8
    graph = [[] for _ in range(N+1)]
    distance = [INF for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    
    for s, e, w in road:
        graph[s].append((e, w))
        graph[e].append((s, w))
    
    graph[1].sort(key=lambda x : -x[1])

    for e, w in graph[1]:
        distance[e] = w
    
    for _ in range(N-1):
        idx = get_smallest_node(graph, distance, visited, N)
        visited[idx] = True
        
        for nxtNode in graph[idx]:
            if distance[idx] + nxtNode[1] < distance[nxtNode[0]]:
                distance[nxtNode[0]] = distance[idx] + nxtNode[1]
    
    for i in range(2, N+1):
        if distance[i] <= K:
            answer += 1
    return answer + 1
    
def get_smallest_node(graph, distance, visited, N):
    idx = 0
    minVal = 10**8
    
    for i in range(2, N+1):
        if not visited[i] and distance[i] < minVal:
            idx = i
            minVal = distance[i]
    
    return idx

    
    