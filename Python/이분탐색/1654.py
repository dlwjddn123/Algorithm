N, K = map(int, input().split())
LAN = []
for _ in range(N):
    n = int(input())
    LAN.append(n)

st, en = 1, max(LAN)
while st <= en:
    total = 0
    mid = (st+en) // 2
    for n in LAN:
        total += n // mid
    if total >= K:
        st = mid + 1
    else:
        en = mid - 1

print(en)