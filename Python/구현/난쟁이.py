dwarfs = []
for _ in range(9):
    N = int(input())
    dwarfs.append(N)

tall = sum(dwarfs)
a, b = 0, 0
ok = False
for i in range(8):
    if ok:
        break
    for j in range(i+1,9):
        if (tall - (dwarfs[i]+dwarfs[j])) == 100:
            a = dwarfs[i]
            b = dwarfs[j]
            ok = True
            break
dwarfs.remove(a)
dwarfs.remove(b)
dwarfs.sort()

for n in dwarfs:
    print(n)

