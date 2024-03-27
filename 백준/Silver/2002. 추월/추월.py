N = int(input())
start = dict()
s = []
end = []
result = 0

for _ in range(N):
    name = input()
    start[name] = False
    s.append(name)
for _ in range(N):
    end.append(input())


p1, p2 = 0, 0
while p2 != N-1:
    if start[s[p2]]:
        p2 += 1
    elif end[p1] != s[p2]:
        result += 1
        start[end[p1]] = True
        p1 += 1
    else:
        p1 += 1
        p2 += 1

print(result)
