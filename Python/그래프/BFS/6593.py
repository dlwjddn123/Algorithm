from collections import deque

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
result = []
def go():
    arr = [[[0]*C for _ in range(R)]for _ in range(L)]
    visited = [[[False]*C for _ in range(R)]for _ in range(L)]

    for i in range(L):
        for j in range(R+1):
            n = list(input())
            if n == []:
                continue
            arr[i][j] = n

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k] == "S":
                    bfs(k, j, i, visited, arr)
                    break

def bfs(x, y, z, visited, arr):
    q = deque([[x, y, z]])
    count = 0
    while q:
        q2 = deque(q.popleft())
        temp = []
        while q2:
            ax = q2.popleft()
            by = q2.popleft()
            cz = q2.popleft()
            if arr[cz][by][ax] == "E":
                result.append(count)
                return
            visited[cz][by][ax] = True
            for i in range(6):
                if 0 <= dx[i] + ax <= C-1 and 0 <= dy[i] + by <= R-1 and 0<= dz[i] + cz <= L-1:
                    if i >= 4:
                        if not visited[cz+dz[i]][by][ax]:
                            visited[cz+dz[i]][by][ax] = True
                            if arr[cz+dz[i]][by][ax] == "." or arr[cz+dz[i]][by][ax] == "E":
                                temp.append(ax)
                                temp.append(by)
                                temp.append(cz+dz[i])

                    else:
                        if not visited[cz][by+dy[i]][ax+dx[i]]:
                            visited[cz][by+dy[i]][ax+dx[i]] = True
                            if arr[cz][by+dy[i]][ax+dx[i]] == "." or arr[cz][by+dy[i]][ax+dx[i]] == "E":
                                temp.append(ax+dx[i])
                                temp.append(by+dy[i])
                                temp.append(cz)
        if len(temp) == 0:
            result.append(0)
            return
        q.append(temp)
        count += 1


while True:
    L, R, C = map(int, input().split())
    if L == 0 and L == R == C:
        break
    go()

for i in range(len(result)):
    if result[i] == 0:
        print("Trapped!")
    else:
        print(f"Escaped in {result[i]} minute(s). ")       


            




