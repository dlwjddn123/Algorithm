N, M = map(int, input().split())
board = list(list(input()) for _ in range(N))
color = {0:"B", 1:"W"}
result = []

def fill(row, col):
    blackFirstCount = 0 
    for y in range(row, row + 8):
        for x in range(col, col + 8):
            if board[y][x] != color[(y + x) % 2]:
                blackFirstCount += 1

    whiteFirstCount = 0 
    for y in range(row, row + 8):
        for x in range(col, col + 8):
            if board[y][x] != color[(y + x + 1) % 2]:
                whiteFirstCount += 1
    return min(blackFirstCount, whiteFirstCount)

for row in range(N-8 + 1):
    for col in range(M-8 + 1):
        result.append(fill(row, col))

print(min(result))