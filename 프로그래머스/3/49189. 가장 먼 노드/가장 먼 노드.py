from collections import deque

def solution(n, edge):
    answer = 0
    node = [0 for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    # count = [0 for _ in range(n + 1)]
    node[1] = 1
    
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    
    
    q1 = deque([graph[1]])
    count = 0
    node[1] = -1
    
    while q1:
        q2 = deque(q1.popleft())
        count += 1
        temp = []
        while q2:
            idx = q2.popleft()
            if node[idx] == 0:
                node[idx] = count
                temp += graph[idx]
        if len(temp) != 0:
            q1.append(temp)
    
    MAX = max(node)
    
    for i in range(len(node)):
        if node[i] == MAX:
            answer += 1
    
    return answer