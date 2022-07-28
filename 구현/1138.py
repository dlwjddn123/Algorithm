N = int(input()) # 어떻게 하는진 알겠는데 구현에서 해맸음..
big = list(map(int,input().split()))
order = [0 for _ in range(N)] # 순서 저장

for i in range(1,N+1): 
    b = big[i-1] # 키 큰 사람의 수를 맞는 지 체크 하기 위한 변수
    count = 0 
    for j in range(N):
        if b == count and order[j] == 0: # 키 큰 사람의 수 조건을 만족하면서 그 자리가 0일 때
            order[j] = i
            break
        elif order[j] == 0: # 키 큰 사람의 자리의 수이므로 count += 1
            count += 1

print(*order)