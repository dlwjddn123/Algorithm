from collections import deque

N = int(input())
exist = set()
words = []
alpha = dict()
for _ in range(N):
    n = list(input())
    q = deque(n)
    words.append(q)

for i in range(N):
    j = len(words[i])
    for _ in range(j):
        W = words[i].popleft()
        if W not in exist:
            alpha[W] = 10 ** len(words[i])
            exist.add(W)
        else:
            alpha[W] += 10 ** len(words[i])
result = []
for i in alpha:
    result.append(alpha[i])

result.sort(reverse=True)
total = 0
num = 9
for n in result:
    total += n*num
    num -= 1

print(total)
