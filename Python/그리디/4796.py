result = []
while True:
    L, P, V = map(int, input().split())
    if L == 0 and L == P == V:
        break
    total = 0
    current = 0
    while True:
        if current + P >= V:
            if V - current <= L:
                total += V - current
            else:
                total += L
            break
        current += P
        total += L
    result.append(total)

for i, n in enumerate(result):
    print(f"Case {i+1}: {n}")
           
             
         