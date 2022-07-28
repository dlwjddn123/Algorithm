from collections import deque


N, M = map(int, input().split())

arr = [[] for i in range(N+1)]
stC = 1
enC = 1000000000
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])

st, en = map(int, input().split())

def bfs(mid):
    global st ,en
    q = deque()
    q.append(st)
    while q:
        idx = q.popleft()
        if idx == en:
            return True
        for nx, nC in arr[idx]:
            if not visited[nx] and mid <= nC:
                q.append(nx)
                visited[nx] = True
    return False

while stC <= enC:
    visited = [False for i in range(N+1)]
    m = (stC+enC) // 2
    if bfs(m):
        stC = m + 1
    else:
        enC = m - 1

print(enC)





        


