import heapq
def solution(n, paths, gates, summits):
    answer = []
    summits = set(summits)
    node = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        node[i].append((j, w))
        node[j].append((i, w))
    min_intensity = [10000001 for _ in range(n + 1)]
    pq = [(0, i) for i in gates]
    while pq:
        intensity, cur_node = heapq.heappop(pq)
        if min_intensity[cur_node] <= intensity:
            continue
        min_intensity[cur_node] = intensity
        if cur_node in summits:
            continue
        for nxt_node, weight in node[cur_node]:
            nxt_intensity = max(intensity, weight)
            if nxt_intensity >= min_intensity[nxt_node]:
                continue       
            heapq.heappush(pq, (nxt_intensity, nxt_node))
    result = []
    for i in summits:
        result.append([i, min_intensity[i]])
    result.sort(key=lambda x : (x[1], x[0]))
    return result[0]