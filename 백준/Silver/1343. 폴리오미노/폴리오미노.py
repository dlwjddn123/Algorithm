N = list(input())
result = ""
count = 0

for i in range(len(N)):
    if N[i] == '.':
        if count == 0:
            result += '.'
            continue
        if count == 1 or count == 3:
            result = ""
            break
        if count == 2:
            result += 'BB.'
            count = 0
            continue
    if N[i] == 'X':
        if count == 3:
            result += 'AAAA'
            count = 0
        else:
            count += 1

if count == 2:
    result += "BB"
    print(result)
elif count == 1 or count == 3 or result == "":
    print(-1)
else:
    print(result)
        