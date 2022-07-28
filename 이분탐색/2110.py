N, C = map(int ,input().split())
house = []
result = []
for _ in range(N):
    n = int(input())
    house.append(n)

house.sort()
st, en = 1, house[-1]

while st <= en :
    temp = house[0]
    mid = (st+en)//2
    count = 1
    for i in range(1,N):
        if temp + mid <= house[i]:
            count += 1
            temp = house[i]

    if count >= C:
        result.append(mid)
        st = mid + 1
    else:
        en = mid - 1
        
print(max(result))
    
        
