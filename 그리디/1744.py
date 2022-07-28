N = int(input())
n = []
p = []
for _ in range(N):
    x = int(input())
    if x <= 0:
        n.append(x)
    else:
        p.append(x)

n.sort()
p.sort(reverse=True)

result = 0
visited1 = [False for _ in range(len(n))]
visited2 = [False for _ in range(len(p))]

for i in range(len(n)):
    if i == len(n) - 1:
        if not visited1[i]:
            result += n[i]
        break

    if not visited1[i]:
        result += n[i]*n[i+1]
        visited1[i], visited1[i+1] = True, True
    
for j in range(len(p)):
    if j == len(p) - 1:
        if not visited2[j]:
            result += p[j]
        break
    
    if not visited2[j]:
        if (p[j]*p[j+1]) > (p[j] + p[j+1]):
            result += p[j]*p[j+1]
            visited2[j], visited2[j+1] = True, True
        else:
            result += p[j] + p[j+1]
            visited2[j], visited2[j+1] = True, True

print(result)
