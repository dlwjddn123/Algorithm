import heapq

N = int(input())
cards = []
for _ in range(N):
    n = int(input())
    heapq.heappush(cards, n)

answer = 0
if N == 1:
    print(0)
else:
    total = 0
    while len(cards) > 1:
        n1 = heapq.heappop(cards)
        n2 = heapq.heappop(cards)
        total += n1 + n2
        heapq.heappush(cards, n1 + n2)
    print(total)