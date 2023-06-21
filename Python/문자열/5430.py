from collections import deque


T = int(input())
result = []
for i in range(T):
    p = list(input())
    n = int(input())
    l = input()
    x = []
    temp = ""
    for j in range(1, len(l)):
        if l[j] == "]":
            if len(l) != 2:
                x.append(int(temp))
                continue
            continue
        if l[j] == "," :
            x.append(int(temp))
            temp = ""
        else:
            temp += l[j]
    c = 0
    r = 0
    q = deque(x)
    chk = False
    for n in p:
        if n == "D":
            c += 1
            if len(x) < c :
                result.append("error")
                chk = True
                break
            else:
                if r % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
        if n == "R":
            r += 1
    if chk:
        continue
    else:
        x = list(q)
        if r % 2 != 0:
            x = x[::-1]
        temp = "["
        for i in range(len(x)):
            if i == len(x) - 1:
                temp += str(x[i])
                continue
            temp += str(x[i])
            temp += ","
        temp += "]"
        result.append(temp)
for n in result:
    print(n)
    
    



