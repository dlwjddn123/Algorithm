from collections import deque


N = int(input())
board = [list(input()) for _ in range(N)]
result = []

def checkX(x, y):
    global board
    q = deque()
    q2 = deque()
    q3 = deque()
    board[y][x], board[y][x+1] = board[y][x+1], board[y][x]
    q.append(x)
    q2.append(y)
    q3.append(y)
    count = 0
    visited = [False for _ in range(N)]
    while q:
        dx = q.popleft()
        visited[dx] = True
        if 0 <= dx + 1 <= N-1 and not visited[dx+1]:
            if board[y][x] == board[y][dx+1]:
                count += 1
                visited[dx+1] = True
                q.append(dx+1)
        if 0 <= dx - 1 <= N-1 and not visited[dx-1]:
            if board[y][x] == board[y][dx-1] :
                count += 1
                visited[dx-1] = True
                q.append(dx-1)
    count2 = 0
    visited = [False for _ in range(N)]
    while q2:
        dy = q2.popleft()
        visited[dy] = True
        if 0 <= dy + 1 <= N-1 and not visited[dy+1]:
            if board[y][x] == board[dy+1][x] :
                count2 += 1
                visited[dy+1] = True
                q2.append(dy+1)
            
        if 0 <= dy - 1 <= N-1 and not visited[dy-1]:
            if board[y][x] == board[dy-1][x]:
                count2 += 1
                visited[dy-1] = True
                q2.append(dy-1)
    count3 = 0
    visited = [False for _ in range(N)]
    while q3:
        dy2 = q3.popleft()
        visited[dy2] = True
        if 0 <= dy2 + 1 <= N-1 and not visited[dy2+1]:
            if board[y][x+1] == board[dy2+1][x+1]:
                count3 += 1
                visited[dy2+1] = True
                q3.append(dy2+1)
            
        if 0 <= dy2 - 1 <= N-1 and not visited[dy2-1]:
            if board[y][x+1] == board[dy2-1][x+1]:
                count3 += 1
                visited[dy2-1] = True
                q3.append(dy2-1)
    board[y][x], board[y][x+1] = board[y][x+1], board[y][x]            
    result.append(max(count, count2, count3))

def checkY(x, y):
    global board
    q = deque()
    q2 = deque()
    q3 = deque()
    board[y][x], board[y+1][x] = board[y+1][x], board[y][x]
    q.append(y)
    q2.append(x)
    q3.append(x)
    count = 0
    visited = [False for _ in range(N)]
    while q:
        dy = q.popleft()
        visited[dy] = True
        if 0 <= dy + 1 <= N-1 and not visited[dy+1]:
            if board[y][x] == board[dy+1][x]:
                count += 1
                visited[dy+1] = True
                q.append(dy+1)
        if 0 <= dy - 1 <= N-1 and not visited[dy-1]:
            if board[y][x] == board[dy-1][x]:
                count += 1
                visited[dy-1] = True
                q.append(dy-1)
    count2 = 0
    visited = [False for _ in range(N)]
    while q2:
        dx = q2.popleft()
        visited[dx] = True
        if 0 <= dx + 1 <= N-1 and not visited[dx+1]:
            if board[y][x] == board[y][dx+1]:
                count2 += 1
                visited[dx+1] = True
                q2.append(dx+1)
            
        if 0 <= dx - 1 <= N-1 and not visited[dx-1]:
            if board[y][x] == board[y][dx-1]:
                count2 += 1
                visited[dx-1] = True
                q2.append(dx-1)
    count3 = 0
    visited = [False for _ in range(N)]
    while q3:
        dx2 = q3.popleft()
        visited[dx2] = True
        if 0 <= dx2 + 1 <= N-1 and not visited[dx2+1]:
            if board[y+1][x] == board[y+1][dx2+1]:
                count3 += 1
                visited[dx2+1] = True
                q3.append(dx2+1)
            
        if 0 <= dx2 - 1 <= N-1 and not visited[dx2-1]:
            if board[y+1][x] == board[y+1][dx2-1]:
                count3 += 1
                visited[dx2-1] = True
                q3.append(dx2-1)

    board[y][x], board[y+1][x] = board[y+1][x], board[y][x]            
    result.append(max(count, count2, count3))    
def check(x, y):
    global board
    q = deque()
    q2 = deque()
    q.append(x)
    q2.append(y)
    count = 0
    visited = [False for _ in range(N)]
    while q:
        dx = q.popleft()
        visited[dx] = True
        if 0 <= dx + 1 <= N-1 and not visited[dx+1]:
            if board[y][x] == board[y][dx+1]:
                count += 1
                visited[dx+1] = True
                q.append(dx+1)
        if 0 <= dx - 1 <= N-1 and not visited[dx-1]:
            if board[y][x] == board[y][dx-1] :
                count += 1
                visited[dx-1] = True
                q.append(dx-1)
    count2 = 0
    while q2:
        dy = q2.popleft()
        visited[dy] = True
        if 0 <= dy + 1 <= N-1 and not visited[dy+1]:
            if board[y][x] == board[dy+1][x]:
                count2 += 1
                visited[dy+1] = True
                q2.append(dy+1)
        if 0 <= dy - 1 <= N-1 and not visited[dy-1]:
            if board[y][x] == board[dy-1][x]:
                count2 += 1
                visited[dy-1] = True
                q2.append(dy-1)
    result.append(max(count, count2))

chk = False
for i in range(N):
    for j in range(N):
        if i + 1 <= N-1 and j + 1 <= N-1:
            check(i, j)
            if board[i][j] != board[i][j+1]:
                checkX(i, j)
            else:
                chk = True
            if board[i+1][j] != board[i+1][j]:
                checkY(i, j)
            else:
                chk = True

print(max(result)+1)
        

