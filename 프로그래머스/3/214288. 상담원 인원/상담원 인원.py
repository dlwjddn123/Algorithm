from collections import deque
import heapq

cases = []

def solution(k, n, reqs):
    answer = 0
    reqs.sort(key=lambda x : [x[0], x[1]])
    findCase([], n, k, 0)
    result = []
    print(reqs)
    for case in cases:
        waitingTime = 0
        mento = [[] for _ in range(k+1)]
        for req in reqs:
            if len(mento[req[2]]) < case[req[2]-1]:
                heapq.heappush(mento[req[2]], req[0] + req[1])
                continue
            
            at = heapq.heappop(mento[req[2]])
            
            if at > req[0]:
                waitingTime += at - req[0]
                heapq.heappush(mento[req[2]], at + req[1])
                continue
            heapq.heappush(mento[req[2]], req[0] + req[1])
            
        result.append(waitingTime)    
    return min(result)

def findCase(cur, n, k, total):
    if len(cur) == k-1:
        temp = cur[:]
        temp.append(n - total)
        cases.append(temp)
        return
    
    for i in range(1, n):
        if total + i >= n:
            continue
        cur.append(i)
        findCase(cur, n, k, total+i)
        cur.pop()
        