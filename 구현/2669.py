arr = [[0 for _ in range(101)] for _ in range(101)] # 색종이와 같은 문제 배열 잘 응용해서 풀면 됨

for _ in range(4):
    ldx, ldy, rux, ruy = map(int, input().split())
    for x in range(ldx, rux):
        for y in range(ldy, ruy):
            arr[x][y] = 1
count = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            count += 1

print(count)