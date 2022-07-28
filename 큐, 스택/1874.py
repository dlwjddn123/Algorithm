N = int(input())
arr = []
for _ in range(N):
    n = int(input())
    arr.append(n)
result = []
temp = []
idx = 1
check = True
for n in arr:
    if not check:
        break
    while True:
        if len(temp) == 0 :
            temp.append(idx)
            idx += 1
            result.append("+")
        if temp[-1] == n:
            temp.pop()
            result.append("-")
            break
        temp.append(idx)
        idx += 1
        result.append("+")
        if temp[-1] > n :
            check = False
            break
if check:
    for n in result:
        print(n)
else:
    print("NO")
        