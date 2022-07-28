N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
A.sort()
result = []
for i in range(M):
    st = 0
    en = N - 1
    while True:
        if st > en :
            result.append(0)
            break       
        
        mid = (st+en) // 2
        if B[i] == A[mid]:
            result.append(1)
            break
        elif B[i] > A[mid]:
            st = mid + 1
        else:
            en = mid - 1


for n in result:
    print(n)