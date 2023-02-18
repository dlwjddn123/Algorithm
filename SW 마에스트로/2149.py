K = input()
KeyMap = []
S = input()
for i in range(len(K)):
    KeyMap.append([K[i], i])

KeyMap.sort(key = lambda x : x[0])

Secret = [[] for _ in range(len(S)//len(K))]
for i in range(len(K)):
    temp = S[i*len(S) // len(K) : i*len(S) // len(K) + len(S) // len(K)]
    for j in range(len(S) // len(K)):
        Secret[j].append([temp[j], KeyMap[i][1]])

for i in range(len(Secret)):
    Secret[i].sort(key = lambda x : x[1])
result = ""
for n in Secret:
    for s in n:
        result += s[0]

print(result)