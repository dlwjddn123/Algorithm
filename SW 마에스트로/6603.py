def go(idx):
    if len(result) == 6:
        print(*result)
        return
    for i in range(idx, len(S)):
        result.append(S[i])
        go(i+1)
        result.pop()

while True:
    result = []
    case = list(map(int, input().split()))
    if len(case) == 1 and case[0] == 0:
        break
    S = case[1:]
    go(0)


