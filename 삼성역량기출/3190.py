from collections import deque

N = int(input())
K = int(input())
MAP = [[0]*(N+1) for _ in range(N+1)]
for _ in range(K):
    n = list(map(int, input().split()))
    MAP[n[0]][n[1]] = 2

L = int(input())
go = []
for _ in range(L):
    n = list(input().split())
    n[0] = int(n[0])
    go.append(n)
go.append([-1, 'F'])

def dummy():
    direction = deque([[0, 1], [1, 0], [0, -1], [-1, 0]])
    dx = 1
    dy = 1
    t = 0
    body = deque()
    body.append([1, 1])
    MAP[dy][dx] = 1
    for g in go:
        while t != g[0]:
            if direction[0][1] != 0:
                nx = dx + direction[0][1]
                if 0 < nx <= N and MAP[dy][nx] != 1:
                    if MAP[dy][nx] == 2:
                        MAP[dy][nx] = 1
                        body.append([dy, nx])
                    else:
                        MAP[dy][nx] = 1
                        y, x = body.popleft()
                        MAP[y][x] = 0
                        body.append([dy, nx])
                    dx = nx
                    t += 1
                else:
                    return t+1
            else:
                ny = dy + direction[0][0]
                if 0 < ny <= N and MAP[ny][dx] != 1:
                    if MAP[ny][dx] == 2:
                        MAP[ny][dx] = 1
                        body.append([ny, dx])
                    else:
                        MAP[ny][dx] = 1
                        y, x = body.popleft()
                        MAP[y][x] = 0
                        body.append([ny, dx])
                    dy = ny 
                    t += 1
                else:
                    return t+1
        if g[1] == 'D':
            temp = direction.popleft()
            direction.append(temp)
        elif g[1] == "L":
            temp = direction.pop()
            direction.appendleft(temp)
        else:
            pass

    return t

print(dummy())