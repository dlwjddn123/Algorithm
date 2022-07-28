from collections import deque

N = int(input())
arr = list(map(int, input().split()))
deq = deque()
deq.extend(x for x in range(2,N+1))
result = [1]
temp = arr[0]
for _ in range(N-1):
    i = temp
    if i > 0:
        deq.rotate(-i+1)
    else:
        deq.rotate(-i)
    n = deq.popleft()
    temp = arr[n-1]
    result.append(n)
print(*result)