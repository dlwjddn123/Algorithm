N = int(input()) # 범위가 크면 다시 생각해봐야 할 듯
M = int(input())
perfect_square = []
Sum = []
for i in range(1,101):
    perfect_square.append(i*i)

for n in perfect_square:
    if N <= n and M >= n:
        Sum.append(n)
    if n > M:
        break
if len(Sum) == 0:
    print(-1)
else:
    print(sum(Sum))
    print(min(Sum)) 
    