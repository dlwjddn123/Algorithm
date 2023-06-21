import sys
import heapq
N = int(sys.stdin.readline())
l_start = []
l_end = []

for _ in range(N):
    start, end = map(int,sys.stdin.readline().split())
    l_start.append(start)
    l_end.append(end)
l_start.sort()
l_end.sort()
print(l_start)
print(l_end)
max_overlap = 0
now_overlap = 0
i,j = 0,0
while i < N and j < N:
    if l_start[i] < l_end[j]:
        now_overlap += 1
        i += 1
    elif l_start[i] > l_end[j]:
        max_overlap = max(max_overlap,now_overlap)
        now_overlap -= 1
        j += 1
    else:
        i += 1
        j += 1
max_overlap = max(max_overlap,now_overlap)        
print(max_overlap)