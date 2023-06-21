from collections import deque
N, K = map(int, input().split())
MAX = 100000
visited = [False for _ in range(MAX + 1)]
def bfs(start, end, time):
    q = deque()
    q.append([start, end, time])
    while q:
        current, target, time = q.popleft()
        visited[current] = True
        if current - 1 >= 0 and not visited[current-1]:
            if current - 1 == target:
                return time + 1
            q.append([current-1, target, time+1])
        if current + 1 <= MAX and not visited[current+1]:
            if current + 1 == target:
                return time + 1
            q.append([current+1, target, time+1])
        if current * 2 <= MAX and not visited[current*2]:
            if current * 2 == target:
                return time + 1
            q.append([current*2, target, time+1])

if N == K:
    print(0)
else:
    print(bfs(N, K, 0))
