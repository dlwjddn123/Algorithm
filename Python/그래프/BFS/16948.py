from collections import deque
N = int(input())
visited = [[False]*N for _ in range(N)]
r = list(map(int,input().split()))
start = r[0:2]
end = r[2:]
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
def bfs(s):
    if start == end:
        print(0)
        return
    q = deque([s])
    count = 0
    while q:
        q2 = deque(q.popleft())
        temp = []
        while q2:
            nx = q2.popleft()
            ny = q2.popleft()
            for i in range(6):
                if 0 <= dx[i] + nx <= N-1 and 0 <= dy[i] + ny <= N-1:
                    if [dx[i] + nx, dy[i] + ny] == end:
                        print(count+1)
                        return
                    if not visited[dy[i] + ny][dx[i] + nx]:
                        visited[dy[i] + ny][dx[i] + nx] = True
                        temp.append(dx[i] + nx)
                        temp.append(dy[i] + ny)
        if len(temp) == 0:
            print(-1)
            return
        q.append(temp)
        count += 1

bfs(start)
            


