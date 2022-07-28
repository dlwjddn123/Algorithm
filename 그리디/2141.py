N = int(input())
XA = []
SUM = 0
for i in range(N):
    n = list(map(int, input().split()))
    XA.append(n)
    SUM += n[1]

XA.sort(key=lambda x:x[0])

count = 0
if SUM % 2 == 0:
    for i in range(N):
        count += XA[i][1]
        if count >= SUM//2:
            print(XA[i][0])
else:
    for i in range(N):
        count += XA[i][1]
        if count > SUM//2:
            print(XA[i][0])
        
    



