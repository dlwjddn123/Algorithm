N, L = map(int, input().split())
points = list(map(int, input().split()))
tail = 0

points.sort()
count = 0
for n in points:
    if (n + 0.5) <= tail :
        continue
    else:
        tail = n - 0.5 + L
        count += 1

print(count)