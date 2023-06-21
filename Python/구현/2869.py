A, B, V = map(int, input().split()) # 실행시간 제한 문제였음
days = 0 
gap = A-B
v = V-B # 낮에 정상에 도착하면 미끄러지지 않으므로 미끄러지는 값을 빼줘야함
days += v//gap
if v//gap < v/gap: # v를 gap으로 나눴을 때 실수 값이 남으면 한 번더 올라야 하므로 //와 /의 차이를 이용해서 실수 값이 남는 지 확인하고 남으면 +1 
    print(days+1)
else:
    print(days)