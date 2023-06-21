import heapq
N = int(input())
heap = []

for i in range(N):
    arr = list(map(int, input().split()))
    if not heap:
        for n in arr:
            heapq.heappush(heap, n)
    else:
        for n in arr:
            if heap[0] < n :
                heapq.heappop(heap)
                heapq.heappush(heap, n)
print(heapq.heappop(heap))
