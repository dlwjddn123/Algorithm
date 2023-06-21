from collections import deque

A, B, C = map(int, input().split())
T = max(A,B,C)
visited = [[[False]*(T+1) for _ in range(T+1)] for _ in range(T+1)]

def bfs():
    q = deque([A, B, C])
    while q:
        print(q)
        a = q.popleft()
        b = q.popleft()
        c = q.popleft()
        if a == b and b == c :
            print(1)
            return 
        visited[a][b][c] = True
        if a > b and b+b <= T :
            if not visited[a-b][b+b][c]:
                visited[a-b][b+b][c] = True
                q.extend([a-b, b+b, c])
        elif a < b and a+a <= T:
            if not visited[a+a][b-a][c]:
                visited[a+a][b-a][c] = True
                q.extend([a+a, b-a, c])

        if b > c and c+c <=T:
            if not visited[a][b-c][c+c]:
                visited[a][b-c][c+c] = True
                q.extend([a, b-c, c+c])
        elif b < c and b+b <= T:
            if not visited[a][b+b][c-b]:
                visited[a][b+b][c-b] = True
                q.extend([a, b+b, c-b])

        if a > c  and c+c <=T:
            if not visited[a-c][b][c+c]:
                visited[a-c][b][c+c] = True
                q.extend([a-c, b, c+c])
        elif a < c  and a+a <= T:
            if not visited[a+a][b][c-a]:
                visited[a+a][b][c-a] = True
                q.extend([a+a, b, c-a])
    print(0)
    return
if (A + B + C) % 3 != 0:
    print(0)
else:
    bfs()
