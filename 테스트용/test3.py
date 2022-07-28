n = int(input())
m = list(map(int, input().split()))
find = False
for i in range(n-1, 0, -1):
    if m[i-1] < m[i]:  # 뒷 값이 앞 값보다 크다면
        for j in range(n-1, 0, -1):
            if m[i-1] < m[j]:
                print(i)
                m[i-1], m[j] = m[j], m[i-1]  # 간단한 스왑
                m = m[:i] + sorted(m[i:])  # 이 부분 떄문에 헤맴
                find = True
                break
    if find:
        print(*m)  # 리스트 앞에 *를 붙이면 안에 있는 숫자들을 1 2 3 4 이런 식으로 출력할 수 있음
        break
if not find:
    print(-1)