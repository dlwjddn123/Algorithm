import heapq

def solution(jobs):
    N = len(jobs)
    now = 0
    waiting = []
    count = []
    jobs.sort(reverse=True)
    a = [1,2,3,4]
    
    while len(count) < N:
        while jobs:
            if now >= jobs[-1][0]:
                start, time = jobs.pop()
                heapq.heappush(waiting, (time, start))
            else:
                break
                
        if len(waiting) != 0:
            time, start = heapq.heappop(waiting)
            count.append(now - start + time)
            now += time
            continue
            
        start, time = jobs.pop()
        now = start
        heapq.heappush(waiting, (time, start))
    
    return sum(count) // N

    
    
    
    