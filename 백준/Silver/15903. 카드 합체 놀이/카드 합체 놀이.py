import heapq

N, M = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)

for i in range(M):
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, tmp)
    heapq.heappush(cards, tmp)

print(sum(cards))