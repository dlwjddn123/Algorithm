from collections import deque

A, B, N, M = map(int, input().split())
visited = [False for _ in range(100001)]
move = [-1, 1, -A, -B, A, B, A, B]
q = deque()
q.append([N, 0])
count = 0
while q:
    current, c = q.popleft()
    if current == M:
        count = c
        break
    c += 1
    for i in range(8):
        next = 0
        if i == 6:
            next = current * move[i]
        elif i == 7:
            next = current * move[i]
        else:
            next = move[i] + current
        if 0 <= next <= 100000 and not visited[next]:
            visited[next] = True
            q.append([next, c])

print(count)