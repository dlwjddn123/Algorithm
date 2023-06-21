N = list(input())
result = []
piece = 0
check = False
for i in range(len(N)):
    if check:
        check = False
        continue
    if N[i] == "(":
        if N[i+1] == ")":
            piece += len(result)
            check = True
        else: 
            result.append(N[i])
    else:
        piece += 1
        result.pop()


print(piece)

    




