from collections import deque
import copy


N = int(input())
arr = []
result = 0
r = []
for _ in range(N):
    n = list(map(int, input().split()))
    arr.append(n)

def findMax(A):
    Max = 0
    for i in range(len(A)):
        Max = max(Max,max(A[i])) 
    return Max
    
def up(A, count):
    global result
    for i in range(len(A)):
        temp = []
        for j in range(len(A)):
            if A[j][i] == 0:
                continue
            temp.append(A[j][i])

        for k in range(len(temp)-1):
            if temp[k] == 0:
                continue
            if temp[k] == temp[k+1]:
                temp[k] += temp[k+1]
                temp[k+1] = 0
        a = list(filter(lambda a: a != 0, temp))

        for l in range(len(A)):
            if l < len(a):
                A[l][i] = a[l]
            else:
                A[l][i] = 0
    count += 1
    if count == 5 :
        if result < findMax(A):
            result = findMax(A)
        return
    else:
        cpA1 = copy.deepcopy(A)
        cpA2 = copy.deepcopy(A)
        cpA3 = copy.deepcopy(A)
        cpA4 = copy.deepcopy(A)
        up(cpA1,count)
        down(cpA2,count)
        left(cpA3,count)
        right(cpA4,count)
    

def down(A, count):
    global result
    for i in range(len(A)):
        temp = []
        for j in range(len(A)-1, -1, -1):
            if A[j][i] == 0:
                continue
            temp.append(A[j][i])

        for k in range(len(temp)-1):
            if temp[k] == 0:
                continue
            if temp[k] == temp[k+1]:
                temp[k] += temp[k+1]
                temp[k+1] = 0
        a = list(filter(lambda a: a != 0, temp))
        x = 0
        for l in range(len(A)-1, -1, -1):
            if l > len(A)-1 - len(a):
                A[l][i] = a[x]
            else:
                A[l][i] = 0
            x += 1
    count += 1
    if count == 5 :
        if result < findMax(A):
            result = findMax(A)
        return
    else:
        cpA1 = copy.deepcopy(A)
        cpA2 = copy.deepcopy(A)
        cpA3 = copy.deepcopy(A)
        cpA4 = copy.deepcopy(A)
        up(cpA1,count)
        down(cpA2,count)
        left(cpA3,count)
        right(cpA4,count)

def left(A, count):
    global result
    for i in range(len(A)):
        temp = []
        for j in range(len(A)):
            if A[i][j] == 0:
                continue
            temp.append(A[i][j])

        for k in range(len(temp)-1):
            if temp[k] == 0:
                continue
            if temp[k] == temp[k+1]:
                temp[k] += temp[k+1]
                temp[k+1] = 0
        a = list(filter(lambda a: a != 0, temp))

        for l in range(len(A)):
            if l < len(a):
                A[i][l] = a[l]
            else:
                A[i][l] = 0
    count += 1
    if count == 5 :
        if result < findMax(A):
            result = findMax(A)
        return
    else:
        cpA1 = copy.deepcopy(A)
        cpA2 = copy.deepcopy(A)
        cpA3 = copy.deepcopy(A)
        cpA4 = copy.deepcopy(A)
        up(cpA1,count)
        down(cpA2,count)
        left(cpA3,count)
        right(cpA4,count)   

def right(A, count):
    global result
    for i in range(len(A)):
        temp = []
        for j in range(len(A)-1, -1, -1):
            if A[i][j] == 0:
                continue
            temp.append(A[i][j])

        for k in range(len(temp)-1):
            if temp[k] == 0:
                continue
            if temp[k] == temp[k+1]:
                temp[k] += temp[k+1]
                temp[k+1] = 0
        a = list(filter(lambda a: a != 0, temp))
        x = 0
        for l in range(len(A)-1, -1, -1):
            if l > len(A)-1 - len(a):
                A[i][l] = a[x]
            else:
                A[i][l] = 0
            x += 1
    count += 1
    if count == 5 :
        if result < findMax(A):
            result = findMax(A)
        return
    else:
        cpA1 = copy.deepcopy(A)
        cpA2 = copy.deepcopy(A)
        cpA3 = copy.deepcopy(A)
        cpA4 = copy.deepcopy(A)
        up(cpA1,count)
        down(cpA2,count)
        left(cpA3,count)
        right(cpA4,count)

def go(B):
    global result
    cp1 = copy.deepcopy(B)
    cp2 = copy.deepcopy(B)
    cp3 = copy.deepcopy(B)
    cp4 = copy.deepcopy(B)
    up(cp1, 0)
    down(cp2, 0)
    left(cp3, 0)
    right(cp4, 0)


go(arr)
print(result)