N, M = map(int, input().split()) # 실행속도 줄이기가 쉽지 않구나..
result = 0
NotShuffle = [[False for _ in range(N+1)] for _ in range(N+1)] # 섞이면 안되는 조합 체크하기 위한 배열
for _ in range(M):
    x, y = map(int, input().split()) 
    NotShuffle[x][y] = True # 섞이면 안되는 조합을 True
    NotShuffle[y][x] = True # 앞 뒤 바뀐 조합도 True로 바꿔줘야 함

for i in range(1,N+1): 
    for j in range(i+1,N+1):
        for k in range(j+1,N+1):
            if NotShuffle[i][j] or NotShuffle[j][k] or NotShuffle[i][k]: # i,j,k를 두 개 고른 조합이 NotShuffle에서 True이면 
                continue # pass
            result += 1 # 아니면 +1

print(result)
    