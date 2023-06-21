S = list(input())
P = list(input())
A = [[] for _ in range(123)]
for i in range(len(S)):
    A[ord(S[i])].append(i)

count = 0
idx = 0
while idx < len(P):
    t = P[idx]
    result = 0
    for i in range(len(A[ord(t)])):
        k = 0
        for j in range(len(P)-idx):
            if A[ord(t)][i]+j < len(S):
                if S[A[ord(t)][i]+j] == P[idx+j]:
                    k += 1
                else:
                    break
        if result < k :
            result = k
    count += 1
    idx += result
print(count)