num = set(range(1,10001)) # 무슨 규칙 찾아야대는줄 알고 시간 다잡아먹음; 걍 단순하게 할걸
d = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    d.add(i)

self_num = sorted(num - d)

for n in self_num:
    print(n)
