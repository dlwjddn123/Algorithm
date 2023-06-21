from collections import deque

def bingo_find(i,j):
    total = 0
    for r in range(5):
        if sum(visit[r][0:5]) == 5:
            total += 1

    for c in range(5):
        col = 0
        for r in range(5):
            if visit[r][c] == 1:
                col += 1
            if col == 5:
                total += 1

    right_down = left_down = 0
    for i in range(5):
        if visit[i][i] == 1:
            right_down += 1
        if visit[i][4-i] == 1:
            left_down += 1

    if left_down == 5:
        total += 1
    elif right_down == 5:
        total += 1
    return total

positions = [0]*(26) 
for r in range(5):
    tmp = list(map(int, input().split()))
    for c in range(5):
        positions[tmp[c]] = ((r,c))
numbers =[]

for _ in range(5):
    numbers += list(map(int, input().split()))
numbers = deque(numbers)

cnt = 0 
visit =[[0]*5 for _ in range(5)] 
while numbers:
    num = numbers.popleft()
    cnt +=1
    i,j = positions[num]
    visit[i][j] = 1
    if bingo_find(i,j) >= 3:
        print(cnt)
        break