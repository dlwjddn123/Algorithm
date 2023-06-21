M, N = map(int, input().split())
board = [[1]*M for _ in range(M)]
for i in range(N):
    zero, one, two = map(int, input().split())
    for j in range(1, M+1):
        if zero > 0:
            zero -= 1
            continue
        elif one > 0:
            board[M-j][0] += 1
            one -= 1
            continue
        elif two > 0:
            board[M-j][0] += 2
            two -= 1
            continue
    for k in range(1, M):
        if zero > 0:
            board[0][k] += 0
            zero -= 1
            continue
        elif one > 0:
            board[0][k] += 1
            one -= 1
            continue
        elif two > 0:
            board[0][k] += 2
            two -= 1
            continue

for row in range(1, M):
    for col in range(1, M):
        board[row][col] = board[0][col]
for n in board:
    print(*n)
        
