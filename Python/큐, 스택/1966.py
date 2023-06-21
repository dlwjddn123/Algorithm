from collections import deque
T = int(input())
result = []

for _ in range(T):
    deq = deque()
    N, idx = map(int, input().split())
    deq.extend(list(map(int, input().split())))
    count = 0
    while True:
        check = True
        for j in range(1, len(deq)):
            if deq[0] < deq[j]:
                if idx == 0:
                    idx = len(deq)
                n = deq.popleft()
                deq.append(n)
                check = False
                idx -= 1
                break
        if check:
            count += 1
            deq.popleft()
            if idx == 0:
                result.append(count)
                break
            idx -= 1
for n in result:
    print(n)       





