import heapq


N = int(input())
q = [list(map(int, input().split())) for _ in range(N)]
q.sort(key=lambda x : x[1])
room = [q[0][2]]
for i in range(1, N):
    if room[0] > q[i][1]:
        heapq.heappush(room, q[i][2])
    else:
        heapq.heappop(room)
        heapq.heappush(room, q[i][2])
print(len(room))    



