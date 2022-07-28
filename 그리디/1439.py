S = list(input())
zero = 0
one = 0

temp = int(S[0])
check = False
for i in range(1, len(S)):
    if temp != int(S[i]):
        check = True
        if temp == 0:
            zero += 1
            temp = 1
        else:
            one += 1
            temp = 0

if int(S[-1]) == 0:
    zero += 1
else:
    one += 1

if check:
    print(min(zero, one))
else:
    print(0)