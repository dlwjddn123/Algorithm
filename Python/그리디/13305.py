N = int(input())
distance = list(map(int,input().split()))
oil = list(map(int, input().split()))

total = distance[0] * oil[0]
MIN = oil[0]
for i in range(1, N-1):
    if MIN > oil[i]:
        total += oil[i] * distance[i]
        MIN = oil[i]
    else:
        total += MIN * distance[i]
print(total)
