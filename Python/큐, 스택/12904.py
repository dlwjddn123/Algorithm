from collections import deque

S = input()
T = input()

deq = deque()
deq.extend(T)
deq2 = deque()
deq2.extend(S)

def go(x):
    global S
    if len(x) == len(S):
        if x == deq2:
            print(1)
            return
        else:
            print(0)
            return

    if x[-1] == "A":
        x.pop()
        go(x)
    else:
        x.reverse()
        x.popleft()
        go(x)

go(deq)



        

