import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
idx = 0
fstack = [0 for _ in range(N)]
nfstack = []
for i in range(1, N):
    if A[idx] < A[i]:
        fstack[idx] = A[i]
    else:
        nfstack.append(idx)
    idx += 1

    while len(nfstack) != 0 and A[nfstack[-1]] < A[i]:
        fstack[nfstack.pop()] = A[i]

for i in range(N):
    if fstack[i] == 0:
        fstack[i] = -1

print(*fstack)
