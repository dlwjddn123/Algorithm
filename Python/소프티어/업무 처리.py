from collections import deque

H, K, R = map(int, input().split())
works = [deque(map(int, input().split())) for _ in range(2**H)] # 처음 말단 직원의 업무
staffCount = 2**(H+1) - 1 # 전체 직원의 수
organization = [deque() for _ in range(staffCount+1)] # 1부터 처리하기 위해 +1 
for i in range(len(works)):
    organization[staffCount-i] = works[-i-1] # 말단 직원의 번호에 업무 할당
notEndStaff = 2**(H) # 말단 직원이 아닌 직원의 번호
complete = 0
for day in range(R):
    for t in range(1, notEndStaff): # 탑-다운 방식으로 진행되기 때문에 말단 직원 직전까지만 실행
        if t == 1:
            if len(organization[1]) != 0: # 부서장의 업무 중 처리된 업무가 있다면 그 번호를 더함
                complete += organization[1].popleft()
        if day % 2 == 1 : # 날짜가 홀수일 때
            if len(organization[t*2]) != 0:
                organization[t].append(organization[t*2].popleft())
        elif day % 2 == 0 : # 날짜가 짝수일 때
            if len(organization[t*2+1]) != 0:
                organization[t].append(organization[t*2+1].popleft())
        
print(complete)