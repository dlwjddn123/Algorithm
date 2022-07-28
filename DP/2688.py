T = int(input())
case = []
result = [0,10,55]
arr = [10,9,8,7,6,5,4,3,2,1]
arr2 = []
for _ in range(T):
    n = int(input())
    case.append(n)

for i in range(3,max(case)+1):
    for j in range(10):
        if j == 0:
            arr2.append(result[i-1])
        else:
            arr2.append(arr2[j-1] - arr[j-1])
    result.append(sum(arr2))
    arr = arr2
    arr2 = []

for k in case:
    print(result[k])


    
