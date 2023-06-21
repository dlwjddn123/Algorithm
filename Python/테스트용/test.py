from collections import deque
def fifo():
    for process in process_info:
        for i in range(process[2]):
            print(process[0], end='  ')

def RR(q):
    global process_info, N
    copy_process_info = []
    for n in process_info:
        copy_process_info.append(n[::])
    copy_process_info.sort(key=lambda x : x[1])    
    ready_queue = deque([copy_process_info[0]])
    start = copy_process_info[0][1]
    visited = [False for _ in range(N)] 
    chk = False
    while ready_queue:
        temp = ready_queue.popleft()
        visited[ord(temp[0]) - 65] = True
        for _ in range(q):
            if temp[2] > 0:
                temp[2] -= 1
                chk = True
                print(temp[0], end = ' ')
                start += 1
                for i in range(N):
                    if copy_process_info[i][1] == start and not visited[i]:
                        ready_queue.append(copy_process_info[i])
            else:
                break
        if chk and temp[2] != 0:
            ready_queue.append(temp)

def SPN():
    global process_info
    copy_process_info = []
    for n in process_info:
        copy_process_info.append(n[::])
    copy_process_info.sort(key=lambda x : x[1])
    ready_queue = deque([copy_process_info[0]])
    start = copy_process_info[0][1]
    visited = [False for _ in range(N)]
    while ready_queue:
        s = start
        temp = ready_queue.popleft()
        q = []
        visited[ord(temp[0])-65] = True
        print(s)
        for _ in range(temp[2]):
            s += 1
            print(temp[0], end=' ')
            for i in range(N):
                if copy_process_info[i][1] == s:
                    q.append(copy_process_info[i])

        if len(q) != 0:
            q.sort(key=lambda x : x[2])
            MIN = 2100000000
            for qq in q:
                if qq[1] < MIN : 
                    MIN = qq[1]
                if not visited[ord(qq[0]) - 65]:
                    visited[ord(qq[0]) - 65] = True
                    ready_queue.append(qq)
            
            start = MIN

def HRRN():
    global process_info, N
    copy_process_info = []
    for n in process_info:
        copy_process_info.append(n[::])
    copy_process_info.sort(key=lambda x : x[1])
    ready_queue = deque([copy_process_info[0]])
    start = copy_process_info[0][1]
    visited = [False for _ in range(N)]
    while ready_queue:
        temp = ready_queue.popleft()
        q = []
        MAX = 0
        Alpha = ''
        visited[ord(temp[0])-65] = True
        for _ in range(temp[2]):
            start += 1
            print(temp[0], end=' ')
        for i in range(N):
            if not visited[i] and copy_process_info[i][1] < start:
                q.append(copy_process_info[i])
        for n in q:
            p, wt, bt = n
            if (start - wt + bt) / bt > MAX:
                MAX = (start - wt + bt) / bt
                Alpha = p
        if len(q) != 0:
            ready_queue.append(copy_process_info[ord(Alpha) - 65])

def MLFQ(q):
    global process_info, N
    two_chk = False
    if q == "i":
        two_chk = True
    copy_process_info = []
    for n in process_info:
        copy_process_info.append(n[::])
    copy_process_info.sort(key=lambda x : x[1])
    ready_queue0 = deque([copy_process_info[0]])
    ready_queue1 = deque()
    ready_queue2 = deque()
    ready_queue3 = deque()
    start = copy_process_info[0][1]
    check_sum = 0 
    visited = [False for _ in range(N)]
    while True:
        check_sum = 0 
        for i in range(N):
            if copy_process_info[i][2] == 0:
                check_sum += 1
        if check_sum == N:
            break
        while ready_queue0:
            new_process = False
            chk = False
            if two_chk:
                q = 2 ** 0
            temp = ready_queue0.popleft()
            visited[ord(temp[0]) - 65] = True
            for i in range(q):
                if temp[2] == 0 :
                    break
                start += 1
                temp[2] -= 1
                print(temp[0], end=' ')
                for j in range(N):
                    if not visited[j] and copy_process_info[j][1] == start:
                        chk = True
                        ready_queue1.append(temp)
                        ready_queue0.append(copy_process_info[j])
            if len(ready_queue0) == len(ready_queue1) == len(ready_queue2) == len(ready_queue3) == 0:
                ready_queue0.append(copy_process_info[ord(temp[0]) - 65])
            else:
                if not chk:
                    if temp[2] != 0:
                        ready_queue1.append(temp)

        while ready_queue1:
            if two_chk:
                q = 2 ** 1
            
            chk = False
            temp1 = ready_queue1.popleft()
            for i in range(q):
                if temp1[2] == 0 :
                    break
                start += 1
                print(temp1[0], end=' ')
                temp1[2] -= 1
                for j in range(N):
                    if not visited[j] and copy_process_info[j][1] == start:
                        chk = True
                        if temp1[2] != 0:
                            ready_queue2.append(temp1)
                        ready_queue0.append(copy_process_info[j])
                        new_process = True
            if not chk:
                if temp1[2] != 0:
                    ready_queue2.append(temp1)
            if new_process:
                break
        if new_process:
            continue
        while ready_queue2:
            if two_chk:
                q = 2 ** 2
            temp2 = ready_queue2.popleft()
            chk = False
            for i in range(q):
                if temp2[2] == 0 :
                    break
                start += 1
                print(temp2[0], end=' ')
                temp2[2] -= 1
                for j in range(N):
                    if not visited[j] and copy_process_info[j][1] == start:
                        if temp2[2] != 0:
                            ready_queue3.append(temp2)
                        ready_queue0.append(copy_process_info[j])
                        new_process = True
            if not chk:
                if temp2[2] != 0:
                    ready_queue3.append(temp2)
            if new_process:
                break
        if new_process:
            continue        
        while ready_queue3:
            chk = False
            if two_chk:
                q = 2 ** 3
            temp3 = ready_queue3.popleft()
            for i in range(q):
                if temp3[2] == 0 :
                    break
                start += 1
                print(temp3[0], end=' ')
                temp3[2] -= 1
                for j in range(N):
                    if not visited[j] and copy_process_info[j][1] == start:
                        chk = True
                        if temp3[2] != 0:
                            ready_queue3.append(temp3)
                        ready_queue0.append(copy_process_info[j])
                        new_process = True
            if not chk:
                if temp3[2] != 0:
                    ready_queue3.append(temp3)
            if new_process:
                break

N = int(input())
process_info = []

for i in range(N):
    n = list(map(int,input().split()))
    process_info.append([chr(65+i)] + n)


HRRN()
MLFQ(1)
             
                    
               
                
    




            



