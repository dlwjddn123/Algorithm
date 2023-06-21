V, E = map(int, input().split()) # 정점의 개수 V와 간선이 개수 E을 입력받음
start_node = int(input()) # 시작할 노드의 번호를 입력받음
graph = [[] for _ in range(V+1)] 
visited = [False for _ in range(V+1)] # 방문한 노드인지 체크
dist = [100000000000 for _ in range(V+1)] # 거리를 inf처럼 큰 수로 설정

for i in range(E): # 간선의 개수 만큼 반복
    u, v, w = map(int, input().split()) # u->v로 가는 간선(가중치=w)
    graph[u].append((v, w)) # 노드 정보 append

def get_small_index(): # 시작 노드와 가장 가까운 노드의 인덱스 반환
    index = 0
    MIN = 100000000000
    for i in range(1, V+1): 
        if not visited[i] and dist[i] < MIN:
            MIN = dist[i]
            index = i
    
    return index

def Dijkstra(start): 
    for n in graph[start]: # 거리 값들을 초기화 
        if dist[n[0]] > n[1]: 
            dist[n[0]] = n[1]
 
    dist[start] = 0 # 시작 지점은 0으로 초기화
    visited[start] = True # 시작 노드의 방문을 표시

    for i in range(V-1): # 시작 노드를 제외한 나머지 노드만큼 반복
        current_index = get_small_index()
        visited[current_index] = True # 방문 처리
        for n in graph[current_index]: # 가장 작은 가중치를 가지고 있는 인덱스 값 루프 돌면서
            cost = dist[current_index] + n[1] # 시작부터 현재 노드의 가중치 합의 값과 가려는 노드의 가중치 값을 더하고
            if cost < dist[n[0]] : # 그 값이 원래 있던 거리(dist[?]) 값보다 작을 때
                dist[n[0]] = cost # 거리 값을 업데이트 
        

Dijkstra(start_node)
result = []
for i in range(1, V+1): # 단순하게 무한 값이면 INF를 출력하는 부분
    if dist[i] == 100000000000:
        result.append("INF")
        continue
    result.append(dist[i])

print(result)