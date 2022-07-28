from collections import deque

S = list(input().replace(' ', ''))
C = list(input().replace(' ', ''))
result = 0
idx = 0

while idx + len(C) <= len(S):
    if S[idx] == C[0] and idx+len(C) <= len(S) :
        chk = True
        for j in range(len(C)):
            if C[j] != S[idx+j]:
                chk = False
                break
        if chk:
            idx = idx + len(C)
            result += 1
            continue
    idx += 1

print(result)