N, S = map(int, input().split())
M = list(map(int, input().split()))
count = 0
def go(l, p):
    global count, M
    if p == S and len(l) != len(M):
        count += 1
        
    for i in range(len(l)):
        if i == len(l) - 1:
            if l[i] + p != S:
                return
            else:
                count += 1
                return
        go(l[i+1:], p+l[i])
    return

go(M, 0)
print(count)
