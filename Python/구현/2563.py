# 처음엔 변 길이로 계산하려 했는데 겹치는 부분을 처리하기가 생각보다 복잡해서 문제 보니 크기가 정해져 있었음..
# 배열로 접근해서 푸니 훨씬 수월했음
N = int(input())  
paper = [[0 for _ in range(100)] for _ in range(100)] # 도화지를 배열로 
area = 0 # 넓이
for i in range(N):
    x, y = map(int, input().split())
    for j in range(10): # 색종이 가로, 세로 크기가 10이므로 10번 돌아야 함
        for k in range(10):
            paper[y+j][x+k] = 1 # 그 검은 부분을 1로 표시

for w in range(100):
    for h in range(100):
        if paper[w][h] == 1:
             area += 1

print(area)

