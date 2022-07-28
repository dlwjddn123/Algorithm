from collections import deque


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
result = []
visited = []
def bfs(ry, rx, by, bx):
    q = deque()
    count = 0
    q.append([ry, rx, count, by, bx])
    visited.append((ry, rx, by, bx))
    while q:
        rdy, rdx, c, bdy, bdx = q.popleft()
        if c >= 10:
            continue
        temp = deque()
        for i in range(4):
            nrx, nry = dx[i] + rdx, dy[i] + rdy
            if 0 <= nrx <= M-1 and 0 <= nry <= N-1 :
                if board[nry][nrx] == '#':
                    if board[bdy+dy[i]][bdx+dx[i]] != '#':
                        temp.append([rdy, rdx, c+1, i])
                else:
                    temp.append([rdy, rdx, c+1, i])
        while temp:
            y, x, cnt, d = temp.popleft()
            
            chk1 = False
            chk2 = False

            ny, nx = y, x 
            while True:
                ny += dy[d]
                nx += dx[d]
                if board[ny][nx] == 'O':
                    chk1 = True
                    break
                if board[ny][nx] == '#':
                    ny -= dy[d]
                    nx -= dx[d]
                    break

            nby, nbx = bdy, bdx
            while True:
                nby += dy[d]
                nbx += dx[d]
                if board[nby][nbx] == 'O':
                    chk2 = True
                    break
                
                if board[nby][nbx] == '#':
                    nby -= dy[d]
                    nbx -= dx[d]
                    break

            if nby == ny and nbx == nx:
                if abs(ny - y) + abs(nx - x) > abs(nby - bdy) + abs(nbx - bdx):
                    nx -= dx[d]
                    ny -= dy[d]
                else:
                    nbx -= dx[d]
                    nby -= dy[d]

            if chk1 and not chk2:
                result.append(cnt)
            elif not chk1 and not chk2:
                if (ny, nx, nby, nbx) in visited:
                    continue
                q.append([ny, nx, cnt, nby, nbx])
                visited.append((ny, nx, nby, nbx))
                
            
    if len(result) == 0:
        print(-1)
    else:
        print(min(result))

x1, y1, x2, y2 = 0, 0, 0, 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            x1, y1 = j, i
        if board[i][j] == 'B':
            x2, y2 = j, i
board[y1][x1] = '.'
board[y2][x2] = '.'

bfs(y1, x1, y2, x2)
