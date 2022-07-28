from collections import deque
N, M = map(int, input().split())
select = list(map(int, input().split()))
arr = [x for x in range(1,N+1)]
deq = deque()
deq.extend(arr)
result = 0
for i in range(M):
    middle = len(deq) // 2
    if len(deq) % 2 != 0:
        middle += 1
    idx = deq.index(select[i])
    if idx >= middle:
        deq.rotate(len(deq) - idx)
        result += len(deq) - idx
    else:
        deq.rotate(-idx)
        result += idx 
    deq.popleft()
print(result)


    