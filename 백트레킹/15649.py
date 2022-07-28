N, M = map(int,input().split())
arr = [x for x in range(1,N+1)]

def go(A, Result):
    if len(Result) == M:
        print(*Result)
        return
    
    for n in A:
        cpA = A[:]
        cpResult = Result[:]
        cpA.remove(n)
        cpResult.append(n)
        go(cpA, cpResult)

go(arr, [])


