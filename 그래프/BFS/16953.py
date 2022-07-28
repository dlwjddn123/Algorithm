from collections import deque
A, B = map(int, input().split())

def bfs(a):
    q = deque([[a]])
    count = 0
    while q:
        q2 = deque(q.popleft())
        temp = []
        while q2:
            n = q2.popleft()
            if 2*n == B or int(str(n)+"1") == B:
                print(count+2)
                return
            if 2*n < B:
                temp.append(2*n)
            if int(str(n)+"1") < B:
                temp.append(int(str(n)+"1"))
            else:
                continue
        q.append(temp)
        if len(temp) == 0:
            break
        count += 1
    print(-1)
    return
bfs(A)