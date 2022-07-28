N = int(input())
I = []
for _ in range(N):
    n = list(map(int, input().split()))
    I.append(n)

I.sort(key=lambda x:(x[0], x[1]))
result = 1
present = [I[0]]
for i in range(1,N):
    if present[0][1] > I[i][1]:
        present[0] = I[i]
    elif present[0][1] <= I[i][0]:
        present[0] = I[i]
        result += 1
print(result)
        

