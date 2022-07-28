N = int(input())
perm = list(map(int, input().split()))
chk = False
for i in range(N-1,0,-1):
    if perm[i-1] < perm[i]:      
        for j in range(N-1,0,-1):
            if perm[i-1] < perm[j]:
                perm[j], perm[i-1] = perm[i-1], perm[j]
                chk = True
                A = perm[:i]
                B = sorted(perm[i:])
                perm = A + B
                break
    if chk:
        print(*perm)
if not chk:
    print(-1)

        
