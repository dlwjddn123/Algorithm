N, M = map(int, input().split())
H = list(map(int, input().split()))
st, en = 1, max(H)

while st <= en:
    mid = (st+en) // 2
    total = 0
    for n in H:
        if n > mid :
            total += n - mid
    if total >= M :
        st = mid + 1
    else:
        en = mid - 1

print(en)
