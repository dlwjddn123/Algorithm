roomNumber = list(map(int,input()))
needSet = [0 for _ in range(10)]
for n in roomNumber:
    if n == 6 or n == 9:
        if needSet[6] > needSet[9]:
            needSet[9] += 1
        else:
            needSet[6] += 1
        continue    
    needSet[n] += 1
print(max(needSet))