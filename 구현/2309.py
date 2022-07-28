dwarfs = [] # 범위가 9기 때문에 가능한 방법 dfs도 생각해봤는데 잘 안짜져서 포기, 범위크면 다른방법 생각해봐야 할 듯
for _ in range(9):
    t = int(input())
    dwarfs.append(t)
dwarfs.sort(reverse=True)
for a in range(9-6):
    for b in range(a+1, 9-5):
        for c in range(b+1, 9-4):
            for d in range(c+1, 9-3):
                for e in range(d+1, 9-2):
                    for f in range(e+1, 9-1):
                        for g in range(f+1, 9):
                            if dwarfs[a] + dwarfs[b] + dwarfs[c] + dwarfs[d] + dwarfs[e] + dwarfs[f] + dwarfs[g] == 100:
                                result = ([dwarfs[a], dwarfs[b], dwarfs[c], dwarfs[d], dwarfs[e], dwarfs[f], dwarfs[g]])
                                break
result.sort()
for n in result:
    print(n)