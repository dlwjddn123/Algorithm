from collections import deque

n, w, L = map(int, input().split())
arr = deque()
arr.extend(list(map(int, input().split())))
arr.append(0)
deq = deque()
deq.extend(0 for x in range(w))
T = 0
n = arr.popleft()
while len(arr) != 0:
    if sum(deq) - deq[0] + n <= L:
        deq.popleft()
        deq.append(n)
        n = arr.popleft()
        T += 1
    else:
        deq.popleft()
        deq.append(0)
        T += 1

print(T+len(deq))
