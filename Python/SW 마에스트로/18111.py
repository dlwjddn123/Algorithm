N, M, B = map(int, input().split())
blocks = [0 for _ in range(257)]
field = [list(map(int, input().split()))for _ in range(N)]
for i in range(N):
    for j in range(M):
        blocks[field[i][j]] += 1
MIN = 0
MAX = 0

for i in range(257):
    if blocks[i] >= 1:
        MIN = i
        break

result = []
for j in range(256, -1, -1):
    if blocks[j] >= 1:
        MAX = j
        break

def go(idx):
    global result
    b = B
    t = 0
    for i in range(MAX, idx, -1):
        b += (i - idx) * (blocks[i])
        t += (i - idx) * (blocks[i]) * 2

    for j in range(MIN, idx):
        b -= (idx - j) * (blocks[j])
        t += (idx - j) * (blocks[j])
        if b < 0:
            return
    result.append((t, idx))


for i in range(MAX, MIN-1, -1):
    go(i)
result.sort(key = lambda x : (x[0], -x[1]))
print(f"{result[0][0]} {result[0][1]}")
print(result)
