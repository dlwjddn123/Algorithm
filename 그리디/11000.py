import heapq
n = int(input())

q = []

for i in range(n):
    start, end = map(int, input().split())
    heapq.heappush(q, [start, end])

room = []
x, y = heapq.heappop(q)
heapq.heappush(room, y)

for i in range(1, n):
    x, y = heapq.heappop(q)
    if x < room[0]: 
        heapq.heappush(room, y) 
    else: 
        heapq.heappop(room) 
        heapq.heappush(room, y)

print(len(room))