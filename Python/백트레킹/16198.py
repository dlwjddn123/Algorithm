N = int(input())
energy = list(map(int, input().split()))
result = []

def go(E, Max):
    if len(E) == 2:
        result.append(Max)
        return
    total = []
    for i in range(1, len(E)-1):
        total.append(E[i-1]*E[i+1])
    
    for j in range(len(total)):
        cpE = E[:]
        c = cpE.pop(j+1)
        go(cpE, Max + total[j])

go(energy, 0)
print(max(result))
