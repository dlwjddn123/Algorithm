from collections import deque
N = int(input())
friends = [[0]*(N+1) for _ in range(N+1)]
while True:
    p1, p2 = map(int, input().split())
    if p1 == p2 == -1:
        break
    friends[p1][p2] = 1
    friends[p2][p1] = 1

result = []
for i in range(1, N+1):
    visited = [False for _ in range(N+1)]
    visited[i] = True
    q = deque()
    q.append([i, 0])
    scores = []
    while q:
        x, score = q.popleft()
        scores.append(score)
        for j in range(1, N+1):
            if j == x:
                continue
            if friends[x][j] == 1 and not visited[j]:
                visited[j] = True
                q.append([j, score+1])
    result.append([max(scores), i])

result.sort(key=lambda x : (x[0], x[1]))
a = []
t = result[0][0]
for n in result:
    if n[0] != t:
        break
    a.append(n[1])
print(t, len(a))
print(*a)


