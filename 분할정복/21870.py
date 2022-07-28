N = int(input())
M = list(map(int, input().split()))
result = []
def g(n, m):
    while m:
        n, m = m, n%m
    return n
    
def go(s, c):
    if len(s) == 1:
        result.append(c+s[0])
        return
    t = len(s) // 2
    caseF = s[:t]
    caseB = s[len(s)-1:t-1:-1]
    F = caseF[0]
    B = caseB[0]
    
    for FF in caseF:
        F = g(F, FF)
    for BB in caseB:
        B = g(B, BB)
    go(s[t:], c + F)
    go(s[:t], c + B)
    
    
go(M, 0)
print(max(result))