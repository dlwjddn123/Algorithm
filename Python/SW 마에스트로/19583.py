start, end, endStreaming = map(str, input().split())
time = [start, end, endStreaming]
realTime = []
for n in time:
    realTime.append(int((n[:2]) + (n[3:])))
names = dict()
count = 0
while True:
    try:
        t, name = input().split()
        t = int((t[:2]) + (t[3:]))
        if t <= realTime[0]:
            if name not in names:
                names[name] = 1
            
        elif realTime[1] <= t <= realTime[2]:
            if name in names and names[name] == 1:
                names[name] -= 1
                count += 1
    except:
        break          
print(count)

