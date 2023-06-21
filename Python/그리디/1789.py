S = int(input())
SUM = 0
i = 1
while True:
    SUM += i
    if SUM > S:
        print(i-1)
        break
    elif SUM == S:
        print(i)
        break
    i += 1