N = int(input()) # 문제 잘 읽자.
cards = [n for n in range(1,N+1)]
result = []
while len(cards) != 1:
    result.append(cards.pop(0))
    l = cards.pop(0)
    cards.append(l)
result.append(cards.pop(0))
print(*result) 