import sys # 문자열 처리문제 다룰 땐 sys를 사용하자 훨씬 빠르다

input = sys.stdin.readline 
T = int(input())
result = []
for _ in range(T):
    s = list(input().split())
    case = []
    for i in s:
        rvs = i[::-1]
        case.append(rvs)
    result.append(" ".join(case))

for i in range(T):
    print(result[i])