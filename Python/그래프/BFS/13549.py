import heapq

N, K = map(int, input().split())
visited = [False for _ in range(100001)]

def bfs(start):
    q = [(0, start)]
    while q:
        t, X = heapq.heappop(q)
        if X == K:
            return t
        if X*2 <= 100000 and not visited[X*2]:
            visited[X*2] = True
            heapq.heappush(q, (t, X*2))    
        if X-1 >= 0 and not visited[X-1]:
            visited[X-1] = True
            heapq.heappush(q, (t+1, X-1))    
        if X+1 <= 100000 and not visited[X+1]:
            visited[X+1] = True
            heapq.heappush(q, (t+1, X+1))    

print(bfs(N))