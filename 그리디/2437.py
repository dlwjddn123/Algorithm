N = int(input())
A = list(map(int, input().split()))
A.sort()
t = 1
for n in A:
    if t < n:
        break
    t += n
print(t)