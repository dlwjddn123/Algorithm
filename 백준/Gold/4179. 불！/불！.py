from collections import deque

R, C = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

board = [list(input()) for _ in range(R)]

jx, jy = 0, 0
f = []
for i in range(R):
    for j in range(C):
        if board[i][j] == 'J':
            jx, jy = j, i
            board[i][j] = '.'

        if board[i][j] == 'F':
            f.append((i,j))

def bfs(jx, jy, f_pos):
    visited_j = [[False] * C for _ in range(R)]
    visited_j[jy][jx] = True

    queue_j, queue_f = deque([[(jy, jx, 0)]]), deque([f_pos])
    while queue_j:
        pos_j, pos_f = queue_j.popleft(), queue_f.popleft()
        next_pos_j, next_pos_f = [], []

        for y, x, n in pos_j:
            if board[y][x] == 'F':
                continue

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx > C-1 or ny < 0 or ny > R-1:
                    return n + 1
                if not visited_j[ny][nx] and board[ny][nx] == '.':
                    next_pos_j.append((ny, nx, n + 1))
                    visited_j[ny][nx] = True
            
        for y, x in pos_f:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx <= C-1 and 0 <= ny <= R-1 and board[ny][nx] == '.':
                    next_pos_f.append((ny, nx))
                    board[ny][nx] = 'F'
        
        if len(next_pos_j) != 0:
            queue_j.append(next_pos_j)
        queue_f.append(next_pos_f)
        
    return -1

answer = bfs(jx, jy, f)

if answer == -1:
    print("IMPOSSIBLE")
else:
    print(answer)
