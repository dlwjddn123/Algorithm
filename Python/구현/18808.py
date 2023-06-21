import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
R, C = 0, 0
board = [[0]*M for _ in range(N)]
sticker = []
total = 0
def rotate():
    r = len(sticker)
    c = len(sticker[0])
    result = [[0]*r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            result[j][r-i-1] = sticker[i][j]
    return result

def go():
    result = False
    for i in range(N):
        for j in range(M):
            result = checkAndAttach(j, i)
            if result:
                return True
    return False

def checkAndAttach(x, y):
    global total
    result = []
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 0:
                continue
            nx, ny = x + j, y + i
            if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == 0:
                result.append((nx, ny))
                continue
            else:
                return False
    for c, r in result:
        board[r][c] = 1
        total += 1
    return True

for i in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    result = go()
    if result:
        continue
    for i in range(3):
        sticker = rotate()
        result = go()
        if result:
            break
print(total)

