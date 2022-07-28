N = int(input())
arr = list(map(int, input().split()))
MIN = 2e+9+1
result = []
arr.sort()
st, en = 0, N-1

while st < en:
    left = arr[st]
    right = arr[en]
    SUM = left + right
    if abs(SUM) < MIN:
        MIN = abs(SUM)
        result = [left, right]
    
    if SUM < 0 :
        st += 1
        
    else:
        en -= 1

print(result[0], result[1])




