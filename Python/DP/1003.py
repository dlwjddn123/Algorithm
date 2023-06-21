T = int(input())
arr = []
resultZero = [1,0]
resultOne = [0,1]
for _ in range(T):
    n = int(input())
    arr.append(n)

for i in range(2, max(arr)+1):
    resultZero.append(resultZero[i-1]+resultZero[i-2])
    resultOne.append(resultOne[i-1]+resultOne[i-2])

for n in arr:
    print(resultZero[n], resultOne[n])

    