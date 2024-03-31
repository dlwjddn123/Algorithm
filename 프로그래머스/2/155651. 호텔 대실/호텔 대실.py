from collections import deque
import heapq

def solution(book_time):
    answer = 0
    end_times = []
    
    for i in range(len(book_time)):
        start, end = book_time[i][0].replace(":", ""), book_time[i][1].replace(":", "")
        book_time[i][0], book_time[i][1] = int(start), int(end)
    book_time.sort(key=lambda x : x[0])

    for i in range(len(book_time)):
        if len(end_times) == 0:
            heapq.heappush(end_times, book_time[i][1])
        else:
            for _ in range(len(end_times)):
                t = heapq.heappop(end_times)
                h, m = t // 100, t % 100
                m += 10
                if m >= 60:
                    h += 1
                    m -= 60
                if h < book_time[i][0] // 100 or (h == book_time[i][0] // 100 and m <= book_time[i][0] % 100):
                    continue
                heapq.heappush(end_times, t)
            heapq.heappush(end_times, book_time[i][1])
        if answer < len(end_times):
            answer = len(end_times)
    
    return answer