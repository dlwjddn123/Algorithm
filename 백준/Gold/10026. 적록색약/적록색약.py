from collections import deque
N = int(input())
arr1 = []
arr2 = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
color_blindness = 0
non_color_blindness = 0
for _ in range(N):
    n = list(input())
    arr1.append(n)
    arr2.append(n[:])

def bfs1(x, y):
    global non_color_blindness
    q = deque([x,y])
    visited = []
    color = arr1[y][x]
    while q:
        a = q.popleft()
        b = q.popleft()
        for i in range(4):
            if (dy[i]+b, dx[i] + a) in visited:
                continue
            if 0 <= dy[i] + b <= N-1 and 0 <= dx[i] + a <= N-1:
                if color == arr1[dy[i]+b][dx[i]+a]:
                    arr1[dy[i]+b][dx[i]+a] = 0
                    q.append(dx[i]+a)
                    q.append(dy[i]+b)
                    visited.append((dy[i]+b, dx[i] + a))

    non_color_blindness += 1

def bfs2(x, y):
    global color_blindness
    q = deque([x,y])
    visited = []
    color = arr2[y][x]
    while q:
        a = q.popleft()
        b = q.popleft()
        for i in range(4):
            if (dy[i]+b, dx[i] + a) in visited:
                continue
            if 0 <= dy[i] + b <= N-1 and 0 <= dx[i] + a <= N-1:
                if (color == "R" and arr2[dy[i]+b][dx[i]+a] == "G") or (color == "G" and arr2[dy[i]+b][dx[i]+a] == "R"):
                    arr2[dy[i]+b][dx[i]+a] = 0
                    q.append(dx[i]+a)
                    q.append(dy[i]+b)
                    visited.append((dy[i]+b, dx[i] + a))
                elif color == arr2[dy[i]+b][dx[i]+a]:
                    arr2[dy[i]+b][dx[i]+a] = 0
                    q.append(dx[i]+a)
                    q.append(dy[i]+b)
                    visited.append((dy[i]+b, dx[i] + a))


    color_blindness += 1
for i in range(N):
    for j in range(N):
        if arr1[i][j] != 0:
            bfs1(j,i)
        if arr2[i][j] != 0:
            bfs2(j,i)

print(non_color_blindness, color_blindness)