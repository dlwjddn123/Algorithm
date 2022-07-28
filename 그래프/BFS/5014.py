from collections import deque
import sys
input = sys.stdin.readline
F, S, G, U, D = map(int,input().split())

def bfs(s):
    if s == G:
        print(0)
        return
    q = deque([[s]])
    count = 0
    visited = [False for _ in range(F+1)]
    while q:
        q2 = deque(q.popleft())
        temp = []
        while q2:
            n = q2.popleft()
            if n + U == G or n - D == G:
                print(count + 1)
                return
            if U > 0:
                if n + U <= F:
                    if not visited[n + U]:
                        temp.append(n + U)
                        visited[n + U] = True
            else:
                if n < G:
                    print("use the stairs")
                    return
            if D > 0:
                if n - D > 0:
                    if not visited[n - D]:
                        temp.append(n - D)
                        visited[n - D] = True
            else:
                if n > G:
                    print("use the stairs")
                    return
        if len(temp) == 0:
            print("use the stairs")
            return 
        q.append(temp)
        count += 1
bfs(S)


