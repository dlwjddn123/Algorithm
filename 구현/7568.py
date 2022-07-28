N = int(input()) # 문제 잘읽기
l = []
result = [0 for _ in range(N)] # 0으로 초기화
for _ in range(N):
    x, y = map(int, input().split()) 
    t = (x, y) # x,y를 튜플에 저장
    l.append(t) # 그 튜플을 리스트에 append

for i in range(N):
    count = 1 # 자기보다 높은 사람이 없으면 1이므로 1부터 시작
    for j in range(N):
        if l[i][0] < l[j][0] and l[i][1] < l[j][1]: # 키도 큰 동시에 몸무게도 크면
            count += 1 
    result[i] = count # i번째 사람보다 큰 사람의 명수를 저장

print(*result) 
