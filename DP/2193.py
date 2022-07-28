N = int(input())
S = [0, 1, 1]

for i in range(3, 91):
    n = S[i-1] + S[i-2]
    S.append(n)

print(S[N])