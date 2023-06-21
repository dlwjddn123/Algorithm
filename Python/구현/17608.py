import sys # 막대기 기준을 바꿔줘야 하는 걸 나중에 눈치챔
input = sys.stdin.readline # 문제 잘 이해하기

sticks = []
N = int(input())

for _ in range(N):
    h = int(input())
    sticks.append(h)

start = sticks[-1]
base = start
count = 1
for i in range(N-1,0,-1):
    if sticks[i-1] > base:
        base = sticks[i-1]
        count += 1

print(count)
