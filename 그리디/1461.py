N, M = map(int, input().split())
plus = []
minus = []
arr = list(map(int, input().split()))
Max = 0
result = []
total = 0
for n in arr:
    if abs(n) > abs(Max):
        Max = n
    if n >=0 :
        plus.append(n)
    else:
        minus.append(n)
plus.sort(reverse=True)
minus.sort()

for i in range(0, len(plus), M):
    if plus[i] != Max:
        result.append(plus[i])

for i in range(0, len(minus), M):
    if minus[i] != Max:
        result.append(minus[i])

for n in result:
    total += abs(n) * 2

print(total + abs(Max))
